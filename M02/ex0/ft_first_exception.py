def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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
