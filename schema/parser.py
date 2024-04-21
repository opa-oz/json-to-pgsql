from schema.entity import Entity


def append(source: dict[str, list[str]], key: str, value: str):
    if key not in source:
        source[key] = []

    if value not in source[key]:
        source[key].append(value)

    return


def pinpoint_int(v: int, is_safe: bool = False) -> str:
    # [not-working] byteint - Minimum value is -128. Maximum value is 127.
    # smallint - Minimum value is -32768. Maximum value is 32767.
    # integer - Minimum value is –2147483648. Maximum value is 2147483647.
    # bigint - Minimum value is –9223372036854775808. Maximum value is 9223372036854775807.

    if -128 <= v <= 127 and not is_safe:
        return f'smallint'
    elif -32768 <= v <= 32767 and not is_safe:
        return f'smallint'
    elif -2147483648 <= v <= 2147483647:
        return f'int'

    return f'bigint'


def parse(rdata: list[dict]):
    print("Parse start")

    entities = dict({})
    root_entity = Entity(path='root', children=dict({}), types=set())
    root_entity.one_to_one = True

    entities['root'] = root_entity

    def process_arr(current: Entity, arr: list):
        for v in arr:
            path = f'{current.path}.[]'
            if isinstance(v, dict):
                if path in entities:
                    new_entity = entities[path]
                else:
                    new_entity = Entity(path=path, children=dict({}), types=set())
                    new_entity.one_to_one = True

                    entities[path] = new_entity

                current.types.add(f'ENTITY:{path}')
                process_obj(new_entity, v)
                continue
            if isinstance(v, int):
                current.types.add(pinpoint_int(v, True))
                continue
            if isinstance(v, str) or isinstance(v, float) or isinstance(v, bool):
                current.types.add(type(v).__name__)
                continue

            if v is None:
                current.types.add(type(None).__name__)
                continue

            raise Exception('Unexpected type: ' + type(v).__name__)

    def process_obj(current: Entity, obj: dict):
        for k, v in obj.items():
            path = f'{current.path}.{k}'
            if isinstance(v, dict):
                if path in entities:
                    new_entity = entities[path]
                else:
                    new_entity = Entity(path=path, children=dict({}), types=set())
                    new_entity.one_to_one = True
                    entities[path] = new_entity

                append(current.children, k, f'ENTITY:{path}')
                process_obj(new_entity, v)
                continue

            if isinstance(v, list):
                if path in entities:
                    new_entity = entities[path]
                else:
                    new_entity = Entity(path=path, children=dict({}), types=set())
                    new_entity.one_to_many = True
                    entities[path] = new_entity

                append(current.children, k, f'ENTITY:{path}')
                process_arr(new_entity, v)
                continue

            if isinstance(v, int):
                append(current.children, k, pinpoint_int(v, True))
                continue

            if isinstance(v, str) or isinstance(v, float) or isinstance(v, bool):
                append(current.children, k, type(v).__name__)
                continue

            if v is None:
                append(current.children, k, type(None).__name__)
                continue

            raise Exception('Unexpected type: ' + type(v).__name__)

    for item in rdata:
        if item is None:
            root_entity.nullable = True
            continue

        process_obj(root_entity, item)

    print("Parse end")

    return entities
