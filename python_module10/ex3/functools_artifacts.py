#!/usr/bin/python3
from collections.abc import Callable
from typing import Any
from functools import reduce
import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    try:
        reducer = operations[operation]
    except KeyError as exc:
        raise ValueError(f"Unknown operation: {operation}") from exc

    return reduce(reducer, spells)


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
        ) -> dict[str, Callable[[str], str]]:
    return {
        'fire': functools.partial(base_enchantment, 50, "Fire"),
        'ice': functools.partial(base_enchantment, 50, "Ice"),
        'lightning': functools.partial(base_enchantment, 50, "Lightning"),
    }


def enchantment(power: int, element: str, target: str) -> str:
    return f"{element} enchantment hits {target} with {power} power"


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(data: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def spell_dispatcher_damage(data: int) -> str:
        return f"{data} damage"

    @dispatcher.register(str)
    def enchantment_spell(data: str) -> str:
        return data

    @dispatcher.register(list)
    def multi_cast(data: list[Any]) -> str:
        return f"Multi-cast: {len(data)} spells"

    return dispatcher


def main() -> None:
    print("Testing spell_reducer...")
    spells = [5, 10, 20, 40, 25]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial_enchanter...")

    partial_enchant = partial_enchanter(enchantment)

    print(partial_enchant["fire"]("Goblin"))
    print(partial_enchant["ice"]("Dragon"))
    print(partial_enchant["lightning"]("Troll"))

    print("\nTesting memoized fibonacci")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")

    print(f"Enchantment: {dispatcher('fireball')}")

    multi_cast = dispatcher(["fire", "water", "air"])
    print(multi_cast)

    print(dispatcher({"spell": "fireball"}))


if __name__ == "__main__":
    main()
