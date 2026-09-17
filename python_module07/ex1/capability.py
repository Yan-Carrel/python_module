from abc import ABC, abstractmethod
import ex0


class HealCapability(ABC):
    @abstractmethod
    def heal(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Sproutling(ex0.creatures.Creature, HealCapability):
    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"


class Bloomelle(ex0.creatures.Creature, HealCapability):
    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class HealingCreatureFactory(ex0.CreatureFactory):
    def create_base(self) -> Sproutling:
        return Sproutling("Sproutling", "Grass")

    def create_evolved(self) -> Bloomelle:
        return Bloomelle("Bloomelle", "Grass/Fairy")


class Shiftling(ex0.creatures.Creature, TransformCapability):
    def __init__(self, name: str, _type: str) -> None:
        ex0.creatures.Creature.__init__(self, name, _type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return "Shiftling attacks normally."
        else:
            return "Shiftling performs a boosted strike!"

    def transform(self) -> str:
        self.transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return "Shiftling returns to normal."


class Morphagon(ex0.creatures.Creature, TransformCapability):
    def __init__(self, name: str, _type: str) -> None:
        ex0.creatures.Creature.__init__(self, name, _type)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if not self.transformed:
            return "Morphagon attacks normally."
        else:
            return "Morphagon unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.transformed = False
        return "Morphagon stabilizes its form."


class TransformCreatureFactory(ex0.CreatureFactory):
    def create_base(self) -> Shiftling:
        return Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> Morphagon:
        return Morphagon("Morphagon", "Normal/Dragon")
