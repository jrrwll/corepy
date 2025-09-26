import re
from typing import Any


def camel_to_snake(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def snake_to_camel(name: str) -> str:
    parts = name.split('_')
    return parts[0] + ''.join(part.title() for part in parts[1:])


def camel_to_snake_dict(data: Any) -> Any:
    if isinstance(data, dict):
        return {camel_to_snake(k): camel_to_snake_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [camel_to_snake_dict(item) for item in data]
    else:
        return data


def snake_to_camel_dict(data: Any) -> Any:
    if isinstance(data, dict):
        return {snake_to_camel(k): snake_to_camel_dict(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [snake_to_camel_dict(item) for item in data]
    else:
        return data

