#!/usr/bin/python3.10

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    argc = len(sys.argv)
    if argc <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {argc - 1}")
        count = 1
        while count < argc:
            print(f"Argument {count}: {sys.argv[count]}")
            count += 1
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
