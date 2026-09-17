class Plant():
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0
        self.height_per_grow = height_per_grow

        if height >= 0:
            self._height = height
        else:
            print("Error, height can't be negative")

        if age >= 0:
            self._age = age
        else:
            print("Error, age can't be negative")

        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self.height_per_grow

    def grow_older(self) -> None:
        self._age += 1

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height:.0f}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15, 10, 20)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-4)
    rose.set_age(-6)
    plant_data = f"{rose.get_height():.1f}cm, {rose.get_age()} days old"
    print(f"\nCurrent state: {rose.name}: {plant_data}")
