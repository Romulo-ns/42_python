#!/usr/bin/python3.10

import sys


def main() -> None:
    if len(sys.argv) == 1:
        print("Error: No inventory items provided.")
        return

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
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if total_quantity > 0:
        for item in inventory:
            percentage = inventory[item] / total_quantity * 100
            print(f"Item {item} represents {percentage:.1f}%")

    if inventory:
        first_item = list(inventory.keys())[0]

        most_abundant_item = first_item
        most_abundant_quantity = inventory[first_item]

        least_abundant_item = first_item
        least_abundant_quantity = inventory[first_item]

        for item in inventory:
            quantity = inventory[item]

            if quantity > most_abundant_quantity:
                most_abundant_quantity = quantity
                most_abundant_item = item

            if quantity < least_abundant_quantity:
                least_abundant_quantity = quantity
                least_abundant_item = item

        print(
            f"Item most abundant: {most_abundant_item} "
            f"with quantity {most_abundant_quantity}"
        )

        print(
            f"Item least abundant: {least_abundant_item} "
            f"with quantity {least_abundant_quantity}"
        )

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
