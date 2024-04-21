from dataclasses import dataclass


@dataclass
class Entity:
    path: str
    children: dict[str, list[str]]
    types: set[str]
    one_to_many: bool = False
    one_to_one: bool = False
