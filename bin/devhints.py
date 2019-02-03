import sys

from bin.arguments import ActionInvoker

if __name__ == "__main__":
    ActionInvoker(sys.argv).execute_action()