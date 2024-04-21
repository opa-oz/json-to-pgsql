def rpad(value: str, width: int) -> str:
    return '{message: <{width}}'.format(message=value, width=width)
