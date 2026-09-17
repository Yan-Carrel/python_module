#!/usr/bin/python3
from collections.abc import Callable
from typing import Any, TypedDict


class VaultOps(TypedDict):
    store: Callable[[str, Any], None]
    recall: Callable[[str], Any]


def mage_counter() -> Callable[..., int]:
    count = 0

    def count_now() -> int:
        nonlocal count
        count += 1
        return count
    return count_now


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def accumulate(power: int) -> int:
        nonlocal initial_power
        initial_power += power
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> VaultOps:
    my_dict: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        my_dict[key] = value

    def recall(key: str) -> Any:
        return my_dict.get(key, "Memory not found")
    return {"store": store, "recall": recall}


def main() -> None:
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("Testing mage counter...")
    for i in range(1, 4):
        print(f"counter_a call {i}: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")
    mem_vault = memory_vault()

    print("Store  'secret' = 42")
    mem_vault["store"]("secret", 42)

    try:
        to_recall = "secret"
        print(f"Recall '{to_recall}' {mem_vault['recall']('secret')}")
    except KeyError:
        print(f"Recall '{to_recall}': Memory not found")

    try:
        to_recall = "unknown"
        print(f"Recall '{to_recall}' {mem_vault['recall']('unknown')}")
    except KeyError:
        print(f"Recall '{to_recall}': Memory not found")


if __name__ == "__main__":
    main()
