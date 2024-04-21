import json
from pathlib import Path

from schema.schemer import generate
from schema.sql import sql_table


def test_scheme_basic(snapshot):
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'

    with open(resources_dir / 'schema-sample.json', 'r') as f:
        data = json.load(f)

    pgsql = generate(data, "poor_anime")

    for table in pgsql:
        snapshot.assert_match(sql_table(table))


def test_scheme_advanced(snapshot):
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'

    with open(resources_dir / 'schema-sample2.json', 'r') as f:
        data = json.load(f)

    pgsql = generate(data, "anime")

    for table in pgsql:
        snapshot.assert_match(sql_table(table))
