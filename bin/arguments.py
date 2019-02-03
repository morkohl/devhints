import argparse


__version__ = "0.1"


class ActionInvoker:

    def __init__(self, args):
        parser = argparse.ArgumentParser(description="show hints for configured keys.", prog="devhints")
        parser.add_argument("-v", "--version", action="version", version="%(prog)s %(__version__)")
        parser.add_argument("-a", "--add", nargs=2, dest="add", help="add hints")
        parser.add_argument("-r", "--remove", dest="remove", help="remove hints")
        parser.add_argument("--remove-all", dest="remove_all", action="store_true", help="remove all hints")
        parser.add_argument("hint", nargs="?")
        parser.add_argument("-u", "--use", dest="use_file", help="use a different file or url for a key")

        self.parsed_args = parser.parse_args(args[1:])

    @staticmethod
    def remove_own_filename_if_present(args):
        print("args[0]", args[0])
        print("__file__", __file__)
        if args[0] in __file__ or __file__ in args[0]:
            print("found!")
            return list(filter(lambda arg: args.index(arg) != 0, args))
        return args

    def execute_action(self):
        args = self.parsed_args

        if args.hint:
            print("hint", args.hint)
        elif args.use_file:
            print("use_file", args.use_file)

        elif args.add:
            print("add", args.add)
        elif args.remove:
            print("remove", args.remove)
        elif args.remove_all:
            print("remove_all", args.remove_all)
