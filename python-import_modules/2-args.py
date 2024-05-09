#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]  # Ignore le premier argument qui est le nom du script
    arg_count = len(args)
    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
