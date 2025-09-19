import inspect
from abc import ABCMeta, abstractmethod
from enum import StrEnum
from typing import Annotated, get_type_hints

from pydantic import BaseModel, PositiveInt

from corepy.lang import find_sub_types, strip_type, walk_and_import_modules


class Type(StrEnum):
    A = "a"
    B = "b"
    C = "c"
    D = "d"


class Box(BaseModel):
    type: str = Annotated[str, "a,b"]
    value: str = Annotated[str, "c,d"]
    name: str = Annotated[str, Type.A, Type.B]
    port: PositiveInt | None = None


def model_provider_registry(cls):
    if not hasattr(cls, 'providers'):
        cls.providers = {}

    cls.providers[cls.__name__.lower()] = cls
    return cls


class PluginRegistry(ABCMeta):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not hasattr(cls, "plugins"):
            cls.plugins = []  # 存储所有插件类
        else:
            cls.plugins.append(cls)  # 注册新插件


@model_provider_registry
class Plugin(metaclass=PluginRegistry):

    @abstractmethod
    def say(self) -> None:
        pass


@model_provider_registry
class MyPlugin1(Plugin):

    def say(self) -> None:
        print("MyPlugin1")


class MyPlugin2(Plugin):

    def say(self) -> None:
        print("MyPlugin2")


def test_registry():
    hints = get_type_hints(Box)
    print(f"\n{hints}")

    annotations = inspect.get_annotations(Box)
    print(f"\n{annotations}")

    print(f"\nplugins:\n{Plugin.plugins}")
    for plugin_cls in Plugin.plugins:
        print(f"{plugin_cls} -> {plugin_cls()}")

    print(f"\nproviders:\n{Plugin.providers}")


def test_walk_and_import_modules():
    print("\nwalk_and_import_modules")
    import corepy

    for m in walk_and_import_modules(corepy):
        for attr_name in dir(m):
            attr = getattr(m, attr_name)
            if isinstance(attr, type):
                print(attr)


def test_find_sub_types():
    print("\nfind_sub_types")
    import tests

    classes = find_sub_types(Plugin, tests)
    for cls in classes:
        print(cls)


def test_strip_type():
    print(f"\nBox: {strip_type(Box)}")
    for name, info in Box.model_fields.items():
        print(f"{name}: {strip_type(info.annotation)}")
