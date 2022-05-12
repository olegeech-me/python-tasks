#!/usr/bin/env python3

import sys
from collections import deque

def tail(filename, n=10):
    with open(filename) as fh:
        return deque(fh, n)

def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print(f"Usage: {sys.argv[0]} /path/to/file")
        sys.exit(-1)

    for line in tail(filename):
        print(line.rstrip('\n'))

if __name__ == "__main__":
    main()
