import argparse
import os

from hintutil import HintUtil


__version__ = "0.1"


class ActionInvoker:

    def __init__(self, args):
        #args = ActionInvoker.remove_own_filename_if_present(args)

        parser = argparse.ArgumentParser(description="show hints for configured keys.", prog="devhints")
        parser.add_argument("-v", "--version", action="version", version="%(prog)s %(__version__)")
        parser.add_argument("-a", "--add", nargs=2, dest="add", help="add hints")
        parser.add_argument("-r", "--remove", dest="remove", help="remove hints")
        parser.add_argument("--remove-all", dest="remove_all", action="store_true", help="remove all hints")
        parser.add_argument("-l", "--list", dest="list", action="store_true", help="list all hints and their values")
        parser.add_argument("hint", nargs="?")

        self.hint_util = HintUtil()
        self.default_json_file = os.environ["HOME"] + "/.local/share/devhints/hints.json"
        self.parsed_args = parser.parse_args(args)

    def execute_action(self):
        args = self.parsed_args

        if args.hint:
            self.hint_util.open_hint(args.hint)
        elif args.list:
            self.hint_util.list_hints()
        elif args.add:
            self.hint_util.add_hint(args.binadd[0], args.add[1])
        elif args.remove:
            self.hint_util.remove_hint(args.remove)
        elif args.remove_all:
            print("remove_all", args.remove_all)
