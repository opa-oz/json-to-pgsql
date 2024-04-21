import json
from pathlib import Path

from schema import parse
from schema.encoder import EnhancedJSONEncoder


def test_parse_basic(snapshot):
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'

    with open(resources_dir / 'sample.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    snapshot.assert_match(json.dumps(schema, indent=2, cls=EnhancedJSONEncoder))


def test_parse_deep(snapshot):
    base_dir = Path.cwd()
    resources_dir = base_dir / 'resources'

    with open(resources_dir / 'sample2.json', 'r') as f:
        data = json.load(f)

    schema = parse(data)
    snapshot.assert_match(json.dumps(schema, indent=2, cls=EnhancedJSONEncoder))
