import json
from schema.encoder import EnhancedJSONEncoder
from schema.entity import Entity
from schema.sql import Column, Table
from schema.utils import to_snake_case

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
    parts = [to_snake_case(p) for p in parts if p != "[]"]  # remove ".[]"

    is_root = table_name == 'root'

    if not is_root:
        parts = parts[1:]

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
        column = Column(name=to_snake_case(key))
        # map types from Python to PostgreSQL (exclude - types started with "ENTITY:")
        types: list[str] = [mappings[t] if S not in t else t for t in seen_types]

        _, column = decide_type(types, column, entity.path)

        if not column.nullable:
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


def get_id_column(table) -> Column:
    for c in table.columns:
        if c.name == "id":
            return c

    raise Exception(f'Table {table} does not have an id column')


def generate(schema: dict[str, dict], alias: str) -> list[Table]:
    tables: list[Table] = []
    qs_tables: dict[str, int] = dict()

    def find_foreign_tables(table_key: str) -> list[Table]:
        typestr = f'{S}{table_key}'
        matchesstr = set()
        matches = []

        for t in tables:
            for c in t.columns:
                if c.type == typestr:
                    if t.name in matchesstr:
                        break
                    matchesstr.add(t.name)
                    matches.append(t)
                    break

        return list(matches)

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

            foreign_tables = find_foreign_tables(key)
            foreign_keys = []
            for t in foreign_tables:
                foreign_keys.append(Column(
                    name=f"{t.name}_id",
                    foreign_key=t.name,
                    type=get_id_column(t).type
                ))

            table = Table(name=table_name, order=100, smth_to_many=True, columns=[
                Column(name="id", type="serial", autoincrement=True, nullable=False, unique=False, primary_key=True),
                column
            ])
            table.columns += foreign_keys
            qs_tables[table_name] = len(tables)
            tables.append(table)

    for key, _entity in schema.items():
        # Next process *-to-many (a.k.a. nested arrays)
        entity = Entity(**_entity)
        if entity.one_to_one:
            continue

        table_name = get_table_name(f"{key}.m2m", alias)
        types_joined = ",".join(entity.types)

        if S in types_joined:  # like "root.genres.[]", where it's must many-to-many
            if "," in types_joined:
                raise Exception(f'Unexpected combinations of types. Entity: {key}, types: {types_joined}')

            external_key = key.replace(".[]", "")
            foreign_tables = find_foreign_tables(external_key)
            foreign_keys = []
            for t in foreign_tables:
                foreign_keys.append(Column(
                    name=f"{t.name}_id",
                    foreign_key=t.name,
                    type=get_id_column(t).type
                ))

            column = Column(name=table_name)
            table = Table(name=table_name, order=100, smth_to_many=True, columns=[
                Column(name="id", type="serial", autoincrement=True, nullable=False, unique=False, primary_key=True),
                column
            ])
            table.columns += foreign_keys
            qs_tables[table_name] = len(tables)
            tables.append(table)

            for ftable in foreign_tables:
                ftable.order += 1 + table.order
            #     for column in ftable.columns:
            #         # print("===", column.name, column.type, " === ", external_key)
            #         if S + external_key == column.type:
            #             column.type = f"{S}{key}"
            #             # print('HIT', ftable.name, column.type)

            # types should contain only 1 value, which starts with "ENTITY:"
            target_table_name = get_table_name(types_joined, alias)
            target_table = tables[qs_tables[target_table_name]]
            target_table.smth_to_many = True
            # target_table.order += 1 + table.order
            # id_column = get_id_column(target_table)
            #
            # column.type = id_column.type
            # column.foreign_key = target_table_name

            # replace table link to "<table>_m2m" table
            # presumably_target_table = S + key.replace(".[]", "")
            #
            # for table in tables:
            #     for column in table.columns:
            #         if S in column.type and presumably_target_table == column.type:
            #             column.type = f"{S}{key}.m2m"

    for table in tables:
        for column in table.columns:
            if S in column.type:
                target_table_name = get_table_name(column.type, alias)
                index = qs_tables[target_table_name]
                target_table = tables[index]

                if target_table.smth_to_many:
                    # @todo: delete column completely, for now - just fill it with char
                    column.type = 'char(8)'
                    column.nullable = True
                    continue

                target_table.order += 1 + table.order
                id_column = get_id_column(target_table)

                column.type = id_column.type
                column.foreign_key = target_table_name

    tables = sorted(tables, key=lambda t: -t.order)

    return tables
