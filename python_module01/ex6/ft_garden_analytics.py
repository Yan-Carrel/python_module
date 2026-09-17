class Plant:
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float) -> None:
        self.name = name
        self._height = height
        self._age = age
        self.height_per_grow = height_per_grow
        self.stats = Plant.Stats()

        if height >= 0:
            self._height = height
        else:
            print("Error, height can't be negative")

        if age >= 0:
            self._age = age
        else:
            print("Error, age can't be negative")

    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def add_grow(self) -> None:
            self._grow += 1

        def add_age(self) -> None:
            self._age += 1

        def add_show(self) -> None:
            self._show += 1

        def display(self, name: str) -> None:
            print(f"[statistics for {name}]")
            print(
                f"Stats: {self._grow} grow, "
                f"{self._age} age, {self._show} show"
                )

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")
        self.stats.add_show()

    def grow(self, days: int = 1) -> None:
        self._height += self.height_per_grow * days
        self.stats.add_grow()

    def grow_older(self, days: int = 1) -> None:
        self._age += days
        self.stats.add_age()

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

    def show_extra_stats(self) -> None:
        pass

    @staticmethod
    def check_age(age: int) -> None:
        result = False
        if age > 365:
            result = True
        print(f"Is {age} days more than a year? -> {result}")

    @classmethod
    def anonymous(cls) -> "Plant":
        return (cls("Unknown plant", 0, 0, 0))


class Flower(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float, color: str) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.color = color
        self.bloomed = False
        self.seed = 0

    def bloom(self) -> None:
        self.bloomed = True
        self.seed += 42

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Seed(Flower):
    def __init__(
            self, name: str, height: float, age: int,
            height_per_grow: float, color: str) -> None:
        super().__init__(name, height, age, height_per_grow, color)
        self.seed = 0

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed}")


class Tree(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float,
            trunk_diameter: float) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.trunk_diameter = trunk_diameter
        self._shade_count = 0

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diameter:.1f}cm wide."
            )
        self._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def show_extra_stats(self) -> None:
        print(f" {self._shade_count} shade")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float, harvest_season: str,
            nutritional_value: int) -> None:
        super().__init__(name, height, age, height_per_grow)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self, days: int = 1) -> None:
        super().grow(days)
        self.nutritional_value += 1

    def grow_older(self, days: int = 1) -> None:
        super().grow_older(days)
        self.nutritional_value += 1


def statistic(plant: Plant) -> None:
    plant.stats.display(plant.name)
    plant.show_extra_stats()


if __name__ == "__main__":
    flower: Flower = Flower("Rose", 15, 10, 8, "red")
    tree: Tree = Tree("Oak", 200, 365, 0.16, 5)
    seed: Seed = Seed("Sunflower", 80, 45, 1.5, "yellow")
    anonymous: Plant = Plant.anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)

    print("\n=== Flower")
    flower.show()
    statistic(flower)
    print("[asking the rose to grow and bloom]")
    flower.bloom()
    flower.grow()
    flower.show()
    statistic(flower)

    print("\n=== Tree")
    tree.show()
    statistic(tree)
    print(f"[asking the {tree.name} to produce shade]")
    tree.produce_shade()
    statistic(tree)

    print("\n=== Seed")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.bloom()
    seed.grow_older(20)
    seed.grow(20)
    seed.show()
    statistic(seed)

    print("\n=== Anonymous")
    anonymous.show()
    statistic(anonymous)
