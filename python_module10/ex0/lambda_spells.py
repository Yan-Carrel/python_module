#!/usr/bin/python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(
    mages: list[dict[str, Any]],
        min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    most_powerful = max(mages, key=lambda x: x['power'])
    least_powerful = min(mages, key=lambda x: x['power'])
    _max = most_powerful['power']
    _min = least_powerful['power']

    avg_power = (sum(mage['power'] for mage in mages)/len(mages))
    return {
        'max_power': _max, 'min_power': _min,
        'avg_power': float(f"{avg_power:.2f}")
        }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Ice Wand', 'power': 91, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 70, 'type': 'armor'},
        {'name': 'Fire Staff', 'power': 103, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 75, 'type': 'relic'}
        ]
    mages = [
        {'name': 'Phoenix', 'power': 90, 'element': 'lightning'},
        {'name': 'Nova', 'power': 76, 'element': 'ice'},
        {'name': 'Riley', 'power': 58, 'element': 'wind'},
        {'name': 'Riley', 'power': 54, 'element': 'ice'},
        {'name': 'Luna', 'power': 81, 'element': 'lightning'}
        ]
    spells = ['shield', 'freeze', 'tornado', 'meteor']
    print("Testing artifact sorter...")

    sorted_artifacts = []
    for sort_artifact in artifact_sorter(artifacts):
        sorted_artifacts.append(
            f"{sort_artifact['name']} ({sort_artifact['power']} power)"
            )
    print(" < ".join(sorted_artifacts))

    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage_stats")
    print(mage_stats(mages))
