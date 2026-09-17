import random


def get_player_achievements(achievements: list[str]) -> list[str]:
    achievements_len = random.randint(1, len(achievements))

    return random.sample(achievements, achievements_len)


if __name__ == "__main__":
    achievements = [
        "Crafting Genius", "World Savior", "Master Explorer",
        "Collector Supreme",         "Untouchable", "Boss Slayer",
        "Strategist", "Unstoppable", "Speed Runner",
        "Survivor", "Treasure Hunter", "First Steps",
        "Sharp Mind"
        ]
    players: list[set[str]] = [set(), set(), set(), set()]
    names: list[str] = ["Alice", "Bob", "Charlie", "Dylan"]
    print("=== Achievement Tracker System ===\n")

    i: int = 0
    while (i < 4):
        players[i] = set(get_player_achievements(achievements))
        print(f"Player {names[i]}: {players[i]}")
        i += 1

    print(
        "\nAll distinct achievements: "
        f"{set.union(players[0], players[1], players[2], players[3])}"
        )

    common_achievements = set.intersection(
        players[0], players[1], players[2], players[3]
        )
    print(f"\nCommon achievements: {common_achievements}\n")

    print(
        f"Only {names[0]} has:"
        f" {set.difference(players[0], players[1], players[2], players[3])}"
        )
    print(
        f"Only {names[1]} has:"
        f" {set.difference(players[1], players[0], players[2], players[3])}"
        )
    print(
        f"Only {names[2]} has:"
        f" {set.difference(players[2], players[1], players[0], players[3])}"
        )
    print(
        f"Only {names[3]} has:"
        f" {set.difference(players[3], players[1], players[2], players[0])}\n"
        )

    i = 0
    while (i < 4):
        not_present: set[str] = set()
        for achievement in achievements:
            if (achievement not in players[i]):
                not_present = set.union(not_present, {achievement})
        print(f"{names[i]} is missing: {not_present}")
        i += 1
