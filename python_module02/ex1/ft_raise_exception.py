def input_temperature(temp_str: str) -> int:
    result: int = int(temp_str)
    if (result > 40):
        raise ValueError(f"{result}°C is too hot for plants (max 40°C)")
    elif (result < 0):
        raise ValueError(f"{result}°C is too cold for plants (min 0°C)")
    return (result)


def test_temperature(temp_str: str) -> None:
    try:
        result: int = input_temperature(temp_str)
        print(f"Input data is '{temp_str}'")
        print(f"Temperature is now {result}°C\n")
    except ValueError as e:
        print(f"Input data is '{temp_str}'")
        print(f"Caught input_temperature error: {e}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")
