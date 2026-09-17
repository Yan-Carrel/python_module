import random

if __name__ == "__main__":
    names = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
        ]

    all_capitalized = [name.capitalize() for name in names]
    capitalized_names = [name for name in names if name == name.capitalize()]
    capitalized_dict = {
        item: random.randint(1, 1000) for item in all_capitalized
        }

    score_average = sum(
        capitalized_dict.values()) / len(capitalized_dict.values())
    high_scores_dict = {
        name: score for name, score in capitalized_dict.items()
        if score > score_average
        }

    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {names}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {capitalized_names}\n")
    print(f"Score dict: {capitalized_dict}")
    print(f"Score average is {score_average:.2f}")
    print(f"High scores: {high_scores_dict}")
