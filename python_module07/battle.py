#!/usr/bin/python3
import ex0


def create_creature(factory: ex0.CreatureFactory) -> None:
    base_creature = factory.create_base()
    print(base_creature.describe())
    print(base_creature.attack())

    evolved_creature = factory.create_evolved()
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def creatures_fight(
    factory_a: ex0.CreatureFactory,
        factory_b: ex0.CreatureFactory) -> None:
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print(" fight!")
    print(creature_a.attack())
    print(creature_b.attack())


if __name__ == "__main__":
    flameling = ex0.FlameFactory()
    aquabub = ex0.AquaFactory()
    print("Testing factory")
    create_creature(flameling)
    print("\nTesting factory")
    create_creature(aquabub)
    print("\nTesting battle")
    creatures_fight(flameling, aquabub)
