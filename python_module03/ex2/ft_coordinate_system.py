import math


def get_player_pos() -> tuple[float, float, float]:
    coordinates: str = input(
        "Enter new coordinates as floats in format 'x,y,z': "
        )

    try:
        coordinates_list: list[str] = coordinates.split(',')
        if len(coordinates_list) != 3:
            raise ValueError("Invalid syntax")

    except ValueError:
        print("Invalid syntax")
        return get_player_pos()

    for coordinate in coordinates_list:
        try:
            float(coordinate)
        except ValueError:
            print(
                f"Error on parameter '{coordinate}': "
                "could not convert string to float: '{coordinate}'")
            return get_player_pos()
    x, y, z = coordinates_list

    return (float(x), float(y), float(z))


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    tuple1: tuple[float, float, float] = get_player_pos()

    print(f"Got a first tuple: {tuple1}")
    print(f"It includes: X={tuple1[0]}, Y={tuple1[1]}, Z={tuple1[2]}")
    distance_to_center: float = math.sqrt(
        (0 - tuple1[0])**2 + (0 - tuple1[1])**2 + (0 - tuple1[2])**2
        )

    print(f"Distance to center: {distance_to_center:.4f}")
    print("\nGet a second set of coordinates")
    tuple2: tuple[float, float, float] = get_player_pos()
    distance: float = math.sqrt(
        (tuple2[0] - tuple1[0])**2
        + (tuple2[1] - tuple1[1])**2
        + (tuple2[2] - tuple1[2])**2
        )
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
