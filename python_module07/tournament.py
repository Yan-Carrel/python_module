#!/usr/bin/python3
import ex0
import ex1
import ex2
from ex2.strategy import BattleStrategy


def battle(
    opponents: list[
        tuple[
            ex0.CreatureFactory,
            BattleStrategy
            ]
    ]
        ) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved ")

    for opponent_a in opponents:
        index_a = opponents.index(opponent_a)
        base_creature_a = opponent_a[0].create_base()

        for opponent_b in opponents[index_a + 1:]:

            base_creature_b = opponent_b[0].create_base()

            print("\n* Battle *")
            print(base_creature_a.describe())
            print(" vs.")
            print(base_creature_b.describe())
            print(" now fight!")

            try:
                opponent_a[1].act(base_creature_a)
            except ValueError as e:
                print(e)
                return

            try:
                opponent_b[1].act(base_creature_b)
            except ValueError as e:
                print(e)
                return


if __name__ == "__main__":
    flame_factory = ex0.FlameFactory()
    sproutling_factory = ex1.HealingCreatureFactory()
    shiftling_factory = ex1.TransformCreatureFactory()
    aquabub_factory = ex0.AquaFactory()

    normal_strategy = ex2.NormalStrategy()
    aggressive_strategy = ex2.AggressiveStrategy()
    defensive_strategy = ex2.DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle(
        [
            (flame_factory, normal_strategy),
            (sproutling_factory, defensive_strategy)
            ]
            )

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle(
        [
            (flame_factory, aggressive_strategy),
            (sproutling_factory, defensive_strategy)
            ]
        )

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle(
        [
            (aquabub_factory, normal_strategy),
            (sproutling_factory, defensive_strategy),
            (shiftling_factory, aggressive_strategy)
            ]
        )
