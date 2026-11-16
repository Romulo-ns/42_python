#!/usr/bin/python3.10

import sys


def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:

    try:
        if action == "read":
            with open(filename, "r") as file:
                content = file.read()
                return True, content
        elif action == "write":
            with open(filename, "w") as file:
                file.write(content)
                return True, "Content successfully written to file"
        else:
            return False, "invalid action"
    except OSError as error:
        return False, f"{error}"


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_vault_security.py <filename>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Security ===")

    success, message = secure_archive(filename)

    if success:
        print(message)
    else:
        print(f"Error: {message}")
        return

    success, message = secure_archive(
        "archive.txt",
        "write",
        "Hello 42!"
    )

    if success:
        print(message)
    else:
        print(f"Error: {message}")
        return


if __name__ == "__main__":
    main()
