#!/usr/bin/python3.10

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    argc = len(sys.argv)
    count = 1
    if argc <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        for i in sys.argv:
            print(f"Argument {count}: {i}")
            count += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
