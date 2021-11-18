#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    print("{:d} argument".format(len(sys.argv) - 1), end="")
    if len(sys.argv) == 1:
        print(".")
    elif len(sys.argv) == 2:
        print(":")
    else:
        print("s:")

    for i in range(len(sys.argv) - 1):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
