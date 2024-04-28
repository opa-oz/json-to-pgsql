import json
from pathlib import Path

from schema.encoder import EnhancedJSONEncoder
from schema.parser import parse
from schema.schemer import generate
from schema.sql import sql_table


def bulk_parse():
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'
    output_dir = base_dir / 'output'

    output_dir.mkdir(exist_ok=True)

    with open(resources_dir / 'sample.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    with open(output_dir / 'schema-sample.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    with open(resources_dir / 'anime.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    with open(output_dir / 'schema-sample2.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    with open(resources_dir / 'manga.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    with open(output_dir / 'schema-sample3.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)

    with open(resources_dir / 'mal.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    with open(resources_dir / 'mal-schema.json', 'w') as f:
        json.dump(schema, f, indent=2, cls=EnhancedJSONEncoder)


def bulk_schema():
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'
    output_dir = base_dir / 'output'

    output_dir.mkdir(exist_ok=True)

    with open(resources_dir / 'schema-sample.json', 'r') as f:
        data = json.load(f)

    pgsql = generate(data, "poor_anime")

    for table in pgsql:
        print(sql_table(table))
    print("======\n\n")

    with open(resources_dir / 'schema-sample2.json', 'r') as f:
        data = json.load(f)

    pgsql = generate(data, "anime")

    result = []

    for table in pgsql:
        rs = sql_table(table)
        result.append(rs)

        with open(output_dir / 'anime.sql', 'w') as f:
            f.write("\n\n".join(result))

    with open(resources_dir / 'schema-sample3.json', 'r') as f:
        data = json.load(f)

    pgsql = generate(data, "manga")

    result = []

    for table in pgsql:
        rs = sql_table(table)
        result.append(rs)

        with open(output_dir / 'manga.sql', 'w') as f:
            f.write("\n\n".join(result))

    with open(resources_dir / 'mal-schema.json', 'r') as f:
        data = json.load(f)

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
