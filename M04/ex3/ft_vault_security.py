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
                content = file.read()
                new_content = file.write(content)
                return True, "Content successfully written to file"
        else:
            return False, "invalid action"
    except OSError as error:
        return False, f"{error}"



def main() -> None:
    print("=== Cyber Archives Security ===")



if __name__ == "__main__":
    main()
