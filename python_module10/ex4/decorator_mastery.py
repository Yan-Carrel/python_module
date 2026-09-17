#!/usr/bin/python3
import time
import functools
from typing import Any, ParamSpec, TypeVar
from collections.abc import Callable

P = ParamSpec("P")
R = TypeVar("R")


def spell_timer(func: Callable[P, R]) -> Callable[P, R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(
    min_power: int
    ) -> Callable[
        [Callable[P, str]],
        Callable[P, str]
        ]:
    def decorator(func: Callable[P, str]) -> Callable[P, str]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> str:
            power: Any = kwargs.get("power")

            if power is None:
                power = args[-1]

            if power >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(
    max_attempts: int
    ) -> Callable[
        [Callable[P, Any]],
        Callable[P, Any]
        ]:
    def decorator(func: Callable[P, Any]) -> Callable[P, Any]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
            for i in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if i < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {i}/{max_attempts})"
                            )
                    else:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts"
                            )
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


def create_retry_spell_test() -> Callable[[], str]:
    attempts = 0

    @retry_spell(3)
    def retry_spell_test() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise Exception("Try again")
        return "Waaaaaaagh spelled !"

    return retry_spell_test


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for c in name:
            if c != " " and not c.isalpha():
                return False
        if len(name) < 3:
            return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    mage_guild = MageGuild()
    retry_spell_test = create_retry_spell_test()

    print("Testing spell timer...")
    print(f"Result: {fireball()}")

    print("\nTesting retrying spell...")
    print(retry_spell_test())

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("abc"))
    print(MageGuild.validate_mage_name("ab!"))
    print(mage_guild.cast_spell("Lightning", 15))
    print(mage_guild.cast_spell("fireball", 5))
