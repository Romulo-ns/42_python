#!/usr/bin/python3.10

class GardenError(Exception):
    def __init__(
            self,
            message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(
            self,
            message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(
            self,
            message: str = "Unknown plant error"
    ) -> None:
        super().__init__(message)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")

    print("Testing WaterError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")

    print("Testing WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")

    print("Testing WaterError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as error:
        print(f"Caught {error.__class__.__name__}: {error}\n")

    print("Testing catching all garden errors...")
    




    print("All custom error types work correctly!")



if __name__ == "__main__":
    test_custom_errors()
