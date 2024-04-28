import re


def rpad(value: str, width: int) -> str:
    return '{message: <{width}}'.format(message=value, width=width)


def to_snake_case(name):
    """
    https://stackoverflow.com/a/1176023
    :param name:
    :return:
    """
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub('__([A-Z])', r'_\1', name)
    name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', name)
    return name.lower()
