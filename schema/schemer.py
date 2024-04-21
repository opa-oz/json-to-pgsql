from dataclasses import dataclass

from schema.entity import Entity
from schema.sql import Column, Table

S = 'ENTITY:'
NULL = 'null'

# https://www.postgresql.org/docs/current/datatype.html
# https://www.ibm.com/docs/en/psfa/7.2.1?topic=types-character-strings
mappings = {
    "str": "text",
    "bool": "boolean",
    "float": "double",
    "NoneType": NULL,
    # "byteint": "byteint",
    "smallint": "smallint",
    "integer": "integer",
    "int": "integer",
    "bigint": "bigint",
    "datetime": "date",
}

int_order = [
    # "byteint",
    "smallint",
    "integer",
    "bigint",
    "double"
]

defaults = {
    # "byteint": '0',
    "smallint": '0',
    "integer": '0',
    "bigint": '0',
    "text": "''",
    "boolean": 'FALSE',
    "double": '0.0',
    "date": "CURRENT_DATE",
}


def get_table_name(table_name: str, alias: str) -> str:
    parts = table_name.split(".")  # ex: "root.genres.[]"
    parts[0] = alias  # replace "root" with alias
    parts = [p for p in parts if p != "[]"]  # remove ".[]"

    return "_".join(parts)


def safe_int(types: list[str], path: str) -> str:
    # Ints are ordered by range, from smallint to bigint to double
    # for example, if types = ["smallint", "bigint"], we need to select "bigint"
    int_rates = [int_order.index(t) for t in types if 'int' in t or t == 'double']
    if len(int_rates) == 0:
        raise Exception(f'Unexpected combinations of types. Entity: {path}, types: {types}')

    # Find the highest range amongst types
    return int_order[max(int_rates)]


def decide_type(types: list[str], column: Column, path: str) -> (list[str], Column):
    # If we saw None - field is nullable
    if NULL in types:
        column.nullable = True
        types = [t for t in types if t != NULL]

    # If we removed None, and it's only one type left - use this type
    if len(types) == 1:
        column.type = types[0]
    # If it was only None - let's use "str" as default
    elif len(types) == 0:
        column.type = mappings['str']
    # Otherwise - try to select int
    else:
        column.type = safe_int(types, path)

    return types, column


def get_columns(entity: Entity) -> list[Column]:
    columns: list[Column] = []
    id_seen = False

    for key, seen_types in entity.children.items():
        column = Column(name=key)
        # map types from Python to PostgreSQL (exclude - types started with "ENTITY:")
        types: list[str] = [mappings[t] if S not in t else t for t in seen_types]

        _, column = decide_type(types, column, entity.path)

        if column.nullable:
            if column.type in defaults.keys():
                column.default_value = defaults[column.type]
            else:
                column.default_value = NULL

        if key == "id":  # id should be first
            id_seen = True
            column.primary_key = True
            column.unique = True
            column.nullable = False
            columns.insert(0, column)
        else:
            columns.append(column)

    if not id_seen:  # if "id" is not present, add incremental "id" at first place
        columns.insert(0,
                       Column(name="id", type="serial", autoincrement=True, unique=True, nullable=False,
                              primary_key=True))

    return columns


def generate(schema: dict[str, dict], alias: str) -> list[Table]:
    tables: list[Table] = []
    qs_tables: dict[str, int] = dict()

    for key, _entity in schema.items():
        # First process one-to-one tables (a.k.a. nested dicts)
        entity = Entity(**_entity)
        if entity.one_to_many:
            continue

        table_name = get_table_name(key, alias)
        columns = get_columns(entity)

        qs_tables[table_name] = len(tables)
        tables.append(Table(name=table_name, columns=columns))

    for key, _entity in schema.items():
        # Next process *-to-many (a.k.a. nested arrays)
        entity = Entity(**_entity)
        if entity.one_to_one:
            continue

        table_name = get_table_name(key, alias)
        types_joined = ",".join(entity.types)

        if S not in types_joined:  # like "root.english", where it's must one-to-many
            column = Column(name=table_name.replace(f"{alias}_", ""))
            types: list[str] = [mappings[t] if S not in t else t for t in entity.types]
            _, column = decide_type(types, column, entity.path)

            table = Table(name=table_name, order=100, columns=[
                Column(name="id", type="serial", autoincrement=True, nullable=False, unique=True, primary_key=True),
                column
            ])
            qs_tables[table_name] = len(tables)
            tables.append(table)

    for key, _entity in schema.items():
        # Next process *-to-many (a.k.a. nested arrays)
        entity = Entity(**_entity)
        if entity.one_to_one:
            continue

        table_name = get_table_name(key, alias) + "_m2m"
        types_joined = ",".join(entity.types)

        if S in types_joined:  # like "root.genres.[]", where it's must many-to-many
            if "," in types_joined:
                raise Exception(f'Unexpected combinations of types. Entity: {key}, types: {types_joined}')

            column = Column(name=table_name.replace(f"{alias}_", ""))
            table = Table(name=table_name, order=100, columns=[
                Column(name="id", type="serial", autoincrement=True, nullable=False, unique=True, primary_key=True),
                column
            ])
            qs_tables[table_name] = len(tables)
            tables.append(table)

            # types should contain only 1 value, which starts with "ENTITY:"
            target_table_name = get_table_name(types_joined, alias)
            index = qs_tables[target_table_name]
            target_table = tables[index]
            target_table.order += 1 + table.order
            id_column = target_table.columns[0]

            if id_column.name != 'id':
                raise Exception(f'Column {id_column.name} is not id')

            column.type = id_column.type
            column.foreign_key = target_table_name

            # replace table link to "<table>_m2m" table
            presumably_target_table = S + key.replace(".[]", "")

            for table in tables:
                for column in table.columns:
                    if S in column.type and presumably_target_table == column.type:
                        column.type = f"{S}{key}.m2m"

    for table in tables:
        for column in table.columns:
            if S in column.type:
                target_table_name = get_table_name(column.type, alias)
                index = qs_tables[target_table_name]
                target_table = tables[index]
                target_table.order += 1 + table.order
                id_column = target_table.columns[0]

                if id_column.name != 'id':
                    raise Exception(f'Column {id_column.name} is not id')
                column.type = id_column.type
                column.foreign_key = target_table_name

    tables = sorted(tables, key=lambda t: -t.order)

    return tables
