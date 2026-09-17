#!/usr/bin/python3
import ex1


if __name__ == "__main__":
    healing_factory = ex1.HealingCreatureFactory()
    base_creature = healing_factory.create_base()

    print("Testing Creature with healing capability\n base:")
    print(f"{base_creature.describe()}")
    print(f"{base_creature.attack()}")
    print(f"{base_creature.heal()}")

    print(" evolved:")
    evolved_creature = healing_factory.create_evolved()
    print(f"{evolved_creature.describe()}")
    print(f"{evolved_creature.attack()}")
    print(f"{evolved_creature.heal()}")

    transform_factory = ex1.TransformCreatureFactory()
    transform_base_creature = transform_factory.create_base()

    print("\nTesting Creature with transform capability\n base:")
    print(f"{transform_base_creature.describe()}")
    print(f"{transform_base_creature.attack()}")
    print(f"{transform_base_creature.transform()}")
    print(f"{transform_base_creature.attack()}")
    print(f"{transform_base_creature.revert()}")

    print(" evolved:")
    transform_evolved_creature = transform_factory.create_evolved()
    print(f"{transform_evolved_creature.describe()}")
    print(f"{transform_evolved_creature.attack()}")
    print(f"{transform_evolved_creature.transform()}")
    print(f"{transform_evolved_creature.attack()}")
    print(f"{transform_evolved_creature.revert()}")
