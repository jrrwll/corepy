import enum


class _ArgFlag(enum.IntEnum):
    """
    a magic flag based on bits
    bsd:
        bsd style support.
        treat `aux` as `-a -u -x`
        treat `-ef` as `-e -f`
    list:
        list support
        like `-v video1 video2`
    property:
        map value support
        like: -Da=1 -Db=2
    """
    BOOLEAN = 1
    STRING = 2
    LIST = 3
    PROPERTY = 4


class _Argument():
    def __init__(self, names, usage, flag):
        self.names = names
        self.usage = usage
        self.flag = flag


class _ArgParser():
    """
    the structure is a historical legacy porting from Java,
    so why let it more pythonic ?
    """

    def __init__(self):
        self.__key_argument_map = {}
        self.__key_value_map = {}
        self.__values = []
        self.__names_key_map = {}

    def __getitem__(self, key):
        """
        call the 'parse' method first before you wanna get values
        :param key: key which you pass in the 'add' methods
        :return: value
        """
        return self.__key_value_map[key]

    def __setitem__(self, key, value):
        """
        use it to set the default value
        :param key: key which you pass in the 'add' methods
        :param value: the default value
        :return: None
        """
        self.__key_value_map[key] = value

    def __iter__(self):
        return self.__key_value_map.items().__iter__()

    def add_string(self, key, usage, *names):
        self.__key_argument_map[key] = _Argument(names, usage, _ArgFlag.STRING)
        return self

    def add_bool(self, key, usage, *names):
        self.__key_argument_map[key] = _Argument(names, usage, _ArgFlag.BOOLEAN)
        return self

    def add_list(self, key, usage, *names):
        self.__key_argument_map[key] = _Argument(names, usage, _ArgFlag.LIST)
        return self

    def add_dict(self, key, usage, *names):
        self.__key_argument_map[key] = _Argument(names, usage, _ArgFlag.PROPERTY)
        return self

    def parse(self, args, bsd=False):
        pass
