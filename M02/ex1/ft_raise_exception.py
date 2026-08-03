#!/usr/bin/python3.10

def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        return temp


def test_temperature(temp: str) -> None:
    try:
        print(f"Temperature is now {input_temperature(temp)}°C\n")
    except Exception as error:
        print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")

    print("Input data is '25'")
    test_temperature("25")

    print("Input data is 'abc'")
    test_temperature("abc")

    print("All tests completed - program didn't crash!")

    print("Input data is '100'")
    test_temperature("100")

    print("Input data is '-50'")
    test_temperature("-50")
