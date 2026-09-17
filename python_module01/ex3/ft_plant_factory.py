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
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("Rose", 25, 30, 20)
    oak: Plant = Plant("Oak", 200, 365, 0.16)
    cactus: Plant = Plant("Cactus", 5, 90, 0.14)
    sunflower: Plant = Plant("Sunflower", 80, 45, 15)
    fern: Plant = Plant("Fern", 15, 120, 2.5)
    plants = [rose, oak, cactus, sunflower, fern]
    for i in range(0, 5):
        print("Created: ", end="")
        plants[i].show()
