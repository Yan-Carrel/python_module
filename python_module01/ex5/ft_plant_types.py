class Plant:
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

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self._height += self.height_per_grow

    def grow_older(self) -> None:
        self._age += 1

    def set_height(self, value: int) -> None:
        if value < 0:
            print("Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {self._height}cm")

    def set_age(self, value: int) -> None:
        if value < 0:
            print("Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {self._age} days")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


class Flower(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float,
            color: str) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float,
            trunk_diameter: float) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter}cm wide."
            )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float,
            harvest_season: str) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def grow_older(self) -> None:
        super().grow_older()


if __name__ == "__main__":
    flower: Flower = Flower("Rose", 15, 10, 20, "red")
    tree: Tree = Tree("Oak", 200, 365, 0.16, 5)
    vegetable: Vegetable = Vegetable("Tomato", 5, 10, 2.1, "April")
    print("=== Garden Plant Types ===")
    print("=== Flower ===")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()

    print("\n=== Tree ===")
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()

    print("\n=== Vegetable ===")
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        vegetable.grow()
        vegetable.grow_older()
    vegetable.show()
