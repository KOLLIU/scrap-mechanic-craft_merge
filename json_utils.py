from json5 import dump, loads
from typing import Union


def write_json(obj: Union[dict, list], file_name: str):
    with open(file_name, "w", encoding="utf-8") as file:
        dump(obj, file, indent=1, ensure_ascii=False)


def read_json(file_name: str):
    file = open(file_name, "r", encoding="utf-8")
    to_python = file.read()
    file.close()
    return loads(to_python)
