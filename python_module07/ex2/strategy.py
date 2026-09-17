from abc import ABC, abstractmethod
import ex0.creatures as creatures
import ex1.capability as capability


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: creatures.Creature) -> None:
        pass

    @abstractmethod
    def is_valid(self, creature: creatures.Creature) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def act(self,  creature: creatures.Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this normal strategy"
                )
        else:
            print(creature.attack())

    def is_valid(self, creature: creatures.Creature) -> bool:
        if (
                isinstance(creature, creatures.Creature)):
            return True
        return False


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: creatures.Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
                )
        assert isinstance(creature, capability.TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())

    def is_valid(self, creature: creatures.Creature) -> bool:
        if (
            isinstance(creature, capability.TransformCapability)
                ):
            return True
        return False


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: creatures.Creature) -> None:
        if not self.is_valid(creature):
            raise ValueError(
                "Battle error, aborting tournament: "
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
                )
        assert isinstance(creature, capability.HealCapability)

        print(creature.attack())
        print(creature.heal())

    def is_valid(self, creature: creatures.Creature) -> bool:
        if (
            isinstance(creature, capability.HealCapability) and
            not isinstance(creature, capability.TransformCapability)
                ):
            return True
        return False
