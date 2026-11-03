#!/usr/bin/python3.10

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = {}

    for arg in sys.argv[1:]:
        parts = arg.split(":")

        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue

        try:
            quantity = int(parts[1])
        except ValueError:
            print(f"Quantity error for '{parts[0]}'")
            continue

        item_name = parts[0]

        if item_name in inventory:
            print(f"Redundant item '{item_name}' - discarding")
            continue

        inventory[item_name] = quantity

    print(f"Got inventory: {inventory}")

if __name__ == "__main__":
    main()
