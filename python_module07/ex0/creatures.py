from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, _type: str) -> None:
        self.name = name
        self._type = _type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self._type} type Creature"


class Flameling(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragon(Creature):
    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        return Flameling("Flameling", "Fire")

    def create_evolved(self) -> Pyrodon:
        return Pyrodon("Pyrodon", "Fire/Flying")


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        return Aquabub("Aquabub", "Water")

    def create_evolved(self) -> Torragon:
        return Torragon("Torragon", "Water")
