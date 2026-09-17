class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def check_plant(plant_name: str, is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError(f"The {plant_name} plant is wilting!")


def check_water_level(water_level: int, minimum: int) -> None:
    if water_level < minimum:
        raise WaterError("Not enough water in the tank!")


def start_demo() -> None:
    print("Testing PlantError...")
    try:
        check_plant("tomato", True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        check_water_level(2, 5)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        check_plant("tomato", True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_level(2, 5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    start_demo()
    print("\nAll custom error types work correctly!")
