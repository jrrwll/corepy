import collections

from corepy.conv import to_list as _to_list
from ._ArgParser import _ArgFlag, _ArgParser


class ArgParseError(Exception):
    pass


class ArgParser(_ArgParser):
    pass

    def parse(self, args, bsd=False):
        args = _to_list(args)

        if not args or not len(args):
            return

        self._init_name_key_map()

        shift = collections.deque()
        for arg in args:
            # n, ..., 2, 1
            shift.appendleft(arg)

        # 	handle bsd part
        # like ps -ef ... or ps aux ...
        if bsd:
            arg_name = shift.pop()
            self._parse_bsd_args(arg_name)
            if not len(shift):
                return

        # handle no-bsd part
        # -n default -oyaml --type pom --rm=true --force
        # -Dspring.active.profile=dev -Dlog4j.debug=true
        # -i 1 2 3 --property:key=value extra1 extra2
        while len(shift):
            arg_name = shift.pop()

            # name case
            # --rm = true - -type pom
            if arg_name.startswith("--"):
                self._parse_double_minus(arg_name, shift)
                continue
            # -P3306, -o yml, -f=%h-%m-%s, -Dlogger.level=debug
            elif arg_name.startswith("-"):
                self._parse_minus(arg_name, shift)
                continue
            # extra values
            else:
                self.__values.append(arg_name)
                continue

        self._init_attr_dict()

    def _parse_bsd_args(self, arg_name):
        if arg_name.startswith("-"):
            arg_name = arg_name[1:]

        for name in arg_name:
            key, argument = self._get_key_or_raise(name)
            _assert_bool(argument)
            self.__key_value_map[key] = True

    def _parse_double_minus(self, arg_name, shift):
        # treat argument behind `--` as extra values
        if len(arg_name) == 2:
            self._add_values(shift)
            return

        arg_name = arg_name[2:]
        # the case, not `--rm=true` but `--type pom`
        if "=" not in arg_name:
            key, argument = self._get_key_or_raise(arg_name)
            self._add_all_forward(key, argument, shift)
            return

        # the case, not `--type pom` but `--rm=true`
        ind = arg_name.index("=")
        name = arg_name[:ind]
        key, argument = self._get_key_or_raise(name)

        # the case `--rm=`
        if ind == len(arg_name) - 1:
            if argument.flag == _ArgFlag.BOOLEAN:
                self.__key_value_map[key] = True
                return
            raise ArgParseError()

        # the case `--rm=true`
        value = arg_name[ind + 1:]
        self._add_all(key, argument, value)

    def _parse_minus(self, arg_name, shift):
        # only a `-`
        if len(arg_name) == 1:
            self.__values.append(arg_name)
            return

        arg_name = arg_name[1:]
        name = arg_name[:1]
        key, argument = self._get_key_or_raise(name)

        # the case `-o yaml`
        if len(arg_name) == 1:
            self._add_all_forward(key, argument, shift)
            return

        # the case `-P3306 -f=%h-%m-%s, -Dlogger.level=debug`
        value = arg_name[1:]

        # the case `-P3306`
        if "=" not in arg_name:
            self._add_all(key, argument, value)
            return

        # the case `-f=%h-%m-%s`
        index = arg_name.index("=")
        if index == 0:
            # the case, `-o=`
            if len(value) == 1:
                if argument.flag == _ArgFlag.BOOLEAN:
                    self.__key_value_map[key] = True
                raise ArgParseError()

            value = value[1:]
            self._add_all(key, argument, value)
            return

        # the case, `-Dlogger.level=debug`
        _assert_property(argument)
        hkey = value[:index]
        # the case, `-Dlogger.level=`
        if index == len(value):
            hval = ""
        else:
            hval = value[index + 1]

        self._add_property(key, hkey, hval)

    # ==== ==== ====    ==== ==== ====    ==== ==== ====    ==== ==== ====
    # //// //// ////    //// //// ////    //// //// ////    //// //// ////
    # ==== ==== ====    ==== ==== ====    ==== ==== ====    ==== ==== ====

    def _init_name_key_map(self):
        for (k, v) in self.__key_argument_map.items():
            for n in v.names:
                self.__names_key_map[n] = k

    # add attrs to object
    def _init_attr_dict(self):
        # self.__dict__["_"] = self.__values
        setattr(self, "_", self.__values)
        for k, v in self.__key_value_map.items():
            setattr(self, k, v)
            # self.__dict__[k] = v

    def _add_all(self, key, argument, value):
        _assert_not_property(argument)

        if argument.flag == _ArgFlag.BOOLEAN:
            self._add_bool(key, value)
            return

        if argument.flag == _ArgFlag.STRING:
            self.__key_value_map[key] = value
            return

        if argument.flag == _ArgFlag.LIST:
            self._add_list(key, value)
            return

        assert False

    def _add_all_forward(self, key, argument, shift):
        _assert_not_property(argument)

        if argument.flag == _ArgFlag.BOOLEAN:
            self.__key_value_map[key] = True
            return

        if argument.flag == _ArgFlag.STRING:
            if not len(shift):
                raise ArgParseError()
            self.__key_value_map[key] = shift.pop()
            return

        if argument.flag == _ArgFlag.LIST:
            while len(shift):
                value = shift.pop()
                if value.startswith("-"):
                    shift.append(value)
                    return
                self._add_list(key, value)
            return
        assert False

    def _add_bool(self, key, value):
        value = value.lower()
        if value in ["true", "t", "yes", "y", "1"]:
            self.__key_value_map[key] = True
        elif value in ["false", "f", "no", "n", "0"]:
            self.__key_value_map[key] = False
        else:
            raise ArgParseError()

    def _add_list(self, key, value):
        if key in self.__key_value_map:
            array = self.__key_value_map[key]
            array.append(value)
        else:
            self.__key_value_map[key] = [value]

    def _add_property(self, key, hkey, hval):
            if key in self.__key_value_map:
            map = self.__key_value_map[key]
            map[hkey] = hval
        else:
            self.__key_value_map[key] = {hkey: hval}

    def _add_values(self, shift):
        while len(shift):
            self.__values.append(shift.pop())

    def _get_key_or_raise(self, name):
        if name not in self.__names_key_map:
            raise ArgParseError()

        key = self.__names_key_map[name]
        return key, self.__key_argument_map[key]


def _assert_not_property(argument):
    if argument.flag == _ArgFlag.PROPERTY:
        raise ArgParseError()


def _assert_property(argument):
    if argument.flag != _ArgFlag.PROPERTY:
        raise ArgParseError()


def _assert_bool(argument):
    if argument.flag != _ArgFlag.BOOLEAN:
        raise ArgParseError()
