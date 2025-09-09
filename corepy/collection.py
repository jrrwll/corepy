import os
from typing import Any, Callable, Iterable, Mapping, Optional
from copy import deepcopy


# translate a tuple, dict, or __iter__ object to list
def to_list(obj: Any) -> Optional[list[Any]]:
    if obj is list:
        return obj

    if obj is tuple:
        return list(obj)

    if obj is dict:
        return list(obj.items())

    if isinstance(obj, Iterable):
        _obj = []
        for arg in obj:
            _obj.append(arg)
        return _obj

    return None


def take_limit[T](iterable: Iterable[T], limit: int) -> list[T]:
    output = []
    for doc in iterable:
        if limit == 0:
            break
        limit -= 1

        output.append(doc)
    return output


def partition_list[T](a: list[T], size: int | None = None) -> list[list[T]]:
    n = len(a)
    if not size:
        cpu_count = os.cpu_count()
        if not cpu_count or cpu_count > n or cpu_count < 2:
            return [a]
        size = n // cpu_count

    output = []
    i, n = 0, len(a)
    while i < n:
        output.append(a[i:i + size])
        i += size
    return output


def partition_iterable[T](a: Iterable[T], size: int) -> Iterable[list[T]]:
    output = []
    for i in a:
        output.append(i)
        if len(output) == size:
            yield output
            output = []
    if output:
        yield output


def any_match[T](iterable: Iterable[T],
        predicate: Callable[[T], bool]) -> T | None:
    for i in iterable:
        if predicate(i):
            return i
    return None


def first_not_none[T](mapping: Mapping[str, T], *keys: str) -> T | None:
    for k in keys:
        if k in mapping and mapping[k] is not None:
            return mapping[k]
    return None


def deep_merge_dict(a: dict, b: dict) -> dict:
    c = deepcopy(a)
    for k, v in b.items():
        if k not in c:
            c[k] = deepcopy(v)
        else:
            ov = c[k]
            if isinstance(ov, dict) and isinstance(v, dict):
                c[k] = deep_merge_dict(ov, v)
            elif isinstance(ov, list) and isinstance(v, list):
                c[k] = ov + v
            else:
                c[k] = deepcopy(v) # overwrite
    return c
