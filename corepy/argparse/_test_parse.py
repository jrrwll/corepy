import unittest

from . import ArgParser


class TestArgParse(unittest.TestCase):
    @classmethod
    def get_parser(cls):
        parser = ArgParser()

        parser.add_string("n", "number flag", "n", "number")
        parser.add_string("P", "port flag", "P", "port")

        parser.add_bool("rm", "remove flag", "r", "rm", "remove")
        parser.add_bool("a", "--", "a")
        parser.add_bool("u", "--", "u")
        parser.add_bool("x", "--", "x")

        parser.add_list("o", "output flag", "o", "output")
        parser.add_list("H", "header flag", "H", "header")
        parser.add_list("R", "resource type", "resource", "R")

        parser.add_dict('F', "form flag", "F")

        return parser

    def test_parse(self):
        args = "aux -n3 -o yaml -P6379 --rm=true -owide " + \
               "-H x-opts=gzip -Ffilename=awesome.rb -Ffilemode=777 " + \
               "-R svc ep ds"

        args = args.split()
        args.append("-H")
        args.append("Accept: */*")
        args.append("-H")
        args.append("User-Agent: curl/7.54.0")

        args.append("--")
        args.append("nowarn")
        args.append("noredirect")

        parser = self.get_parser()
        parser.parse(args, bsd=True)

        for k, v in parser:
            print("%s\t%s" % (k, v))

        print("_\t%s" % parser._)

        for k, v in parser.F.items():
            print("F\t%s\t%s" % (k, v))


if __name__ == '__main__':
    unittest.main()
