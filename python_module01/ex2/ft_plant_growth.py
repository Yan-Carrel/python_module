class Plant():
    def __init__(
            self, name: str, height: float,
            age: int, height_per_grow: float) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.height_per_grow = height_per_grow

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: "
            f"{self.height:.1f}cm, {self.age} days old"
            )

    def grow(self) -> None:
        self.height += self.height_per_grow

    def grow_older(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose: Plant = Plant("Rose", 25, 30, 0.8)
    initial_height: float = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.grow_older()
        rose.show()
    print(f"Growth this week: {rose.height - initial_height:.1f}cm")
