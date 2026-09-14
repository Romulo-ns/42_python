#!/usr/bin/python3.10

import math


def validate_syntax(position: list[str], text: str) -> bool:
    if len(position) != 3:
        print(
            f"Enter new coordinates as floats in format 'x,y,z': "
            f"{text}"
        )
        print("Invalid syntax")
        return False
    return True


def validate_float(position: list[str]) -> bool:
    for value in position:
        try:
            float(value)
        except ValueError:
            print(
                f"Enter new coordinates as floats in format 'x,y,z': "
                f"{position[0]},{position[1]},{position[2]}"
            )
            print(
                f"Error on parameter '{value}': "
                f"could not convert string to float: '{value}'"
                )
            return False
    return True


def get_player_pos() -> tuple:
    while (True):
        text = input()
        position = text.split(',')
        if not validate_syntax(position, text):
            continue
        if not validate_float(position):
            continue

        position_tuple = tuple(
            float(value) for value in position
        )
        print(
            f"Enter new coordinates as floats in format 'x,y,z': "
            f"{position_tuple[0]}, {position_tuple[1]}, {position_tuple[2]}"
        )
        return position_tuple


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    _first_position = get_player_pos()

    print(f"Got a first tuple: {_first_position}")
    print(
        f"It includes: "
        f"X={_first_position[0]}, "
        f"Y={_first_position[1]}, "
        f"Z={_first_position[2]}"
    )

    # x
    x = _first_position[0]
    # y
    y = _first_position[1]
    # z
    z = _first_position[2]

    d_center = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print(f"Distance to center: {d_center:.4f}\n")

    print("Get a second set of coordinates")
    _second_position = get_player_pos()

    # x
    x = x - _second_position[0]
    # y
    y = y - _second_position[1]
    # z
    z = z - _second_position[2]

    d_between = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    print(f"Distance between the 2 sets of coordinates: {d_between:.4f}")


if __name__ == "__main__":
    main()


# === Game Coordinate System ===
# Get a first set of coordinates
# Enter new coordinates as floats in format 'x,y,z': hello world
# Invalid syntax
# Enter new coordinates as floats in format 'x,y,z': 1.0 , 2.5, 3.0
# Got a first tuple: (1.0, 2.5, 3.0)
# It includes: X=1.0, Y=2.5, Z=3.0
# Distance to center: 4.0311
# Get a second set of coordinates
# Enter new coordinates as floats in format 'x,y,z': 4,abc,5
# Error on parameter 'abc': could not convert string to float: 'abc'
# Enter new coordinates as floats in format 'x,y,z': 4,5,6
# Distance between the 2 sets of coordinates: 4.9244
