import json
import opyls
from pathlib import Path

from schema.encoder import EnhancedJSONEncoder
from schema.parser import parse
from schema.schemer import generate
from schema.sql import sql_table
from schema.tabler import get_tables_graph


def bulk_parse():
    resources_dir = opyls.basedir('resources')
    output_dir = opyls.basedir('output', True)

    data = opyls.load_json(resources_dir / 'sample.json')

    schema = parse(data)
    with open(output_dir / 'schema-sample.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    data = opyls.load_json(resources_dir / 'anime.json')

    schema = parse(data)
    with open(output_dir / 'schema-sample2.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    data = opyls.load_json(resources_dir / 'manga.json')

    schema = parse(data)
    with open(output_dir / 'schema-sample3.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    data = opyls.load_json(resources_dir / 'mal.json')

    schema = parse(data)
    with open(resources_dir / 'mal-schema.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)


def bulk_schema():
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'
    output_dir = base_dir / 'output'

    output_dir.mkdir(exist_ok=True)

    data = opyls.load_json(resources_dir / 'schema-sample.json')

    pgsql = generate(data, "poor_anime")

    for table in pgsql:
        print(sql_table(table))
    print("======\n\n")

    data = opyls.load_json(resources_dir / 'schema-sample2.json')

    pgsql = generate(data, "anime")

    result = []
    tables = []

    for table in pgsql:
        rs = sql_table(table)
        tables.append(table)
        result.append(rs)

        with open(output_dir / 'anime.sql', 'w') as f:
            f.write("\n\n".join(result))

    with open(output_dir / 'tables.json', 'w') as f:
        json.dump(tables, f, indent=2, cls=EnhancedJSONEncoder)

    get_tables_graph(tables)

    data = opyls.load_json(resources_dir / 'schema-sample3.json')
    pgsql = generate(data, "manga")

    result = []

    for table in pgsql:
        rs = sql_table(table)
        result.append(rs)

        with open(output_dir / 'manga.sql', 'w') as f:
            f.write("\n\n".join(result))

    data = opyls.load_json(resources_dir / 'mal-schema.json')

    pgsql = generate(data, "mal_anime")

    result = []

    for table in pgsql:
        rs = sql_table(table)
        result.append(rs)

        with open(output_dir / 'mal_anime.sql', 'w') as f:
            f.write("\n\n".join(result))


if __name__ == '__main__':
    bulk_parse()
    bulk_schema()
