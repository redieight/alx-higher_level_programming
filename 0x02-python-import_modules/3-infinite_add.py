#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    for r in range(1, len(sys.argv)):
        result += int(sys.argv[r])
    print("{}".format(result))
