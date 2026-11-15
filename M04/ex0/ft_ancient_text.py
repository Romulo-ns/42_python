#!/usr/bin/python3.10

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    print("---\n")

    try:
        file = open(filename, "r")
        content = file.read()
        print(content, end="")
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return


if __name__ == "__main__":
    main()
