import sys
import argparse

__version__  = "0.1"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show hints for configured keys.", prog="devhints")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 2.0")
    parser.add_argument("-a", "--add", nargs=2, dest="add", help="add hints")
    parser.add_argument("-r", "--remove", dest="remove", help="remove hints")
    parser.add_argument("hint", nargs="?")
    parser.add_argument("-u", "--use", dest="use_file", help="use a different file or url for a key")

    args = sys.argv

    if args[0] == __file__ or __file__ in args[0]:
        args = list(filter(lambda arg: args.index(arg) != 0, args))

    parsed_args = parser.parse_args(args)
