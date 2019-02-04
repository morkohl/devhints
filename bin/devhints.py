import os
import sys

from arguments import ActionInvoker


def remove_own_filename_if_present(args):
    if args[0] in __file__ or __file__ in args[0]:
        return list(filter(lambda arg: args.index(arg) != 0, args))
    return args


if __name__ == "__main__":
    args = remove_own_filename_if_present(sys.argv)
    ActionInvoker(args).execute_action()