from dataclasses import dataclass
from enum import IntEnum, auto
import abc
from typing import Self


class ArgFlag(IntEnum):
    """
    a magic flag based on bits
    boolean:
        -a
        -y=false
        --rm
        --rm=true
    string:
        -n
        -n 1
        -n1
        -n=1
    list:
        -v video1 video2
    property:
        -Da=1 -Db=2
    """
    Boolean = auto()
    String = auto()
    List = auto()
    Property = auto()


@dataclass
class Argument:

    names: tuple[str, ...]
    usage: str
    flag: ArgFlag


class ArgParseError(Exception):
    pass


class BaseArgParser(abc.ABC):
    """
    the structure is a historical legacy porting from Java,
    so why let it more pythonic ?
    """

    def __init__(self):
        self._key_argument_map: dict[str, Argument] = {}
        self._key_value_map = {}

    def __getitem__(self, key):
        """
        call the 'parse' method first before you want to get values
        :param key: key which you pass in the 'add' methods
        :return: value
        """
        return self._key_value_map[key]

    def __setitem__(self, key, value):
        """
        use it to set the default value
        :param key: key which you pass in the 'add' methods
        :param value: the default value
        :return: None
        """
        self._key_value_map[key] = value

    def __iter__(self):
        return self._key_value_map.items().__iter__()

    def add_string(self, key: str, usage: str, *names: str) -> Self:
        self._key_argument_map[key] = Argument(names, usage, ArgFlag.String)
        return self

    def add_bool(self, key: str, usage: str, *names: str) -> Self:
        self._key_argument_map[key] = Argument(names, usage, ArgFlag.Boolean)
        return self

    def add_list(self, key: str, usage: str, *names: str) -> Self:
        self._key_argument_map[key] = Argument(names, usage, ArgFlag.List)
        return self

    def add_dict(self, key: str, usage: str, *names: str) -> Self:
        self._key_argument_map[key] = Argument(names, usage, ArgFlag.Property)
        return self

    @abc.abstractmethod
    def parse(self, args):
        pass
