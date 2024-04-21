from dataclasses import dataclass

from schema.utils import rpad


@dataclass
class Column:
    name: str
    foreign_key: str = ""
    type: str = "text"
    default_value: str = ""
    unique: bool = False
    primary_key: bool = False
    nullable: bool = False
    autoincrement: bool = False


@dataclass
class Table:
    name: str
    columns: list[Column]
    order: int = 0


def CREATE_TABLE_IF_NOT_EXISTS(table_name: str) -> str:
    return f'CREATE TABLE IF NOT EXISTS "{table_name}"'


def CREATE_INDEX_IF_NOT_EXISTS(column: Column, table_name: str) -> str:
    return f'CREATE INDEX IF NOT EXISTS "{table_name}_idx" ON "{table_name}" USING btree ("{column.name}");'


def sql_table(table: Table) -> str:
    max_column_name: int = max(len(n.name) for n in table.columns) + 3  # "+"+%s
    max_type_name: int = max(len(n.type) for n in table.columns) + 1  # %s
    columns = []

    for column in table.columns:
        columns.append(
            "".join(
                [
                    rpad(f'"{column.name}"', max_column_name),
                    rpad(column.type, max_type_name),
                    # ' SERIAL' if column.autoincrement else '',
                    ' UNIQUE' if column.unique else '',
                    ' PRIMARY KEY' if column.primary_key else '',
                    f' REFERENCES {column.foreign_key} (id)' if column.foreign_key else "",
                    '' if column.nullable else ' NOT NULL']
            )
        )

    columns = ",\n".join(['\t' + column for column in columns])

    result = f"""
--- order = {table.order}
{CREATE_TABLE_IF_NOT_EXISTS(table.name)}
(
{columns}
) with (oids = false);
{CREATE_INDEX_IF_NOT_EXISTS(table.columns[0], table.name)}
    """

    return result.strip()
