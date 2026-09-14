#!/usr/bin/python3.10
def validate_syntax(position: list[str]) -> bool:
    if len(position) != 3:
        print(
            f"Enter new coordinates as floats in format 'x,y,z': "
            f"{position}"
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
                f"{position[0]}, {position[1]}, {position[2]}"
            )
            print(
                f"Error on parameter '{value}': "
                f"could not convert string to float: '{value}'"
                )
            return False
    return True


def get_player_pos() -> None:
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    while (True):
        text = input()
        position = text.split(',')
        if not validate_syntax(position):
            continue
        if not validate_float(position):
            continue

        first_tuple = tuple(
            float(value) for value in position
        )
        print(
            f"Enter new coordinates as floats in format 'x,y,z': "
            f"{first_tuple[0]}, {first_tuple[1]}, {first_tuple[2]}"
        )
        print(f"Got a first tuple: {first_tuple}")
        return

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


def main() -> None:
    get_player_pos()


if __name__ == "__main__":
    main()
