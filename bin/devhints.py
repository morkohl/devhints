import sys
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show hints for configured keys.")
    parser.add_argument("-a", "--add", dest="add hints")
    parser.add_argument("-r", "--remove", dest="remove hints")
    parser.add_argument("hint")
    parser.add_argument("-u", "--use", dest="use a different file for a key")

    args = sys.argv

    if args[0] == __file__ or __file__ in args[0]:
        print("found!")
        args = list(filter(lambda arg: args.index(arg) != 0, args))

    if len(args) >= 2:
        argname = args[1]
        if argname == "help":
            print("help")
        if argname == "add":
            print("add")
        if argname == "remove":
            print("remove")
        hint = argname
