#!/usr/bin/python3
from collections.abc import Callable


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
        ) -> Callable[[str, int], tuple[str, str]]:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(
    base_spell: Callable[[str, int], str],
        multiplier: int) -> Callable[[str, int], str]:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(
    condition: Callable[[str, int], bool],
        spell: Callable[[str, int], str]) -> Callable[[str, int], str]:
    return (
        lambda target, power: spell(target, power)
        if condition(target, power) else "Spell fizzled"
        )


def spell_sequence(
    spells: list[Callable[[str, int], str]]
        ) -> Callable[[str, int], list[str]]:
    return lambda target, power: [spell(target, power) for spell in spells]


def condition_func(target: str, power: int) -> bool:
    return power >= 15


def main() -> None:
    power = 10
    target = 'Dragon'

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined(target, power)
    print(f"Combined spell result: {combined_result[0]}, {combined_result[1]}")

    print("Testing power amplifier")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Amplified spell result: {mega_fireball(target, power)}")

    print("\nTesting conditional_caster")
    print(conditional_caster(condition_func, fireball)(target, 16))

    print("\nTesting spell sequence")
    print(spell_sequence([fireball, heal])(target, power))


if __name__ == "__main__":
    main()
