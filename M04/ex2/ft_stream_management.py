#!/usr/bin/python3.10

import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    print("---\n")

    try:
        file = open(filename, "r")
        content = file.read()
        print(content, end="")
        print("\n---")
        file.close()
        print(f"File '{filename}' closed.\n")
    except OSError as error:
        print(
            f"[STDERR] Error opening file '{filename}': {error}",
            file=sys.stderr
        )
        return

    print("Transform data:")
    print("---\n")
    new_content = ""

    for char in content:
        if char == "\n":
            new_content += "#"
        new_content += char

    if len(content) > 0 and content[-1] != "\n":
        new_content += "#"

    print(f"{new_content}")
    print("\n---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    output_filename = sys.stdin.readline()
    if len(output_filename) > 0 and output_filename[-1] == "\n":
        output_filename = output_filename[:-1]

    if len(output_filename) <= 0:
        print("Not saving data.")
    else:
        print(f"Saving data to '{output_filename}'")
        try:
            file = open(output_filename, "w")
            file.write(new_content)
            file.close()
        except OSError as error:
            print(
                f"[STDERR] Error opening file '{output_filename}': {error}",
                file=sys.stderr
            )
            print("Data not saved.")
            return

        print(f"Data saved in file '{output_filename}'.")


if __name__ == "__main__":
    main()
