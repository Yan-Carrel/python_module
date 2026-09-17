import random
import typing


def gen_event(
        players: list[str],
        actions: list[str]) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = players[random.randint(0, len(players) - 1)]
        action = actions[random.randint(0, len(actions) - 1)]
        yield (name, action)


def consume_event(
        events: list[tuple[str, str]]
        ) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        to_remove = events[random.randint(0, len(events) - 1)]
        new_list = []
        for ev in events:
            if ev != to_remove:
                new_list += [ev]
        events = new_list
        yield to_remove


if __name__ == "__main__":
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "release"]

    print("=== Game Data Stream Processor ===")
    generator = gen_event(players, actions)
    for i in range(1000):
        event = next(generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    ten_tuples = []
    for i in range(10):
        ten_tuples += [next(generator)]
    print(f"Built list of 10 events: {ten_tuples}")

    for ev in consume_event(ten_tuples):
        print(f"Got event from list: {ev}")

        new_list = []
        for item in ten_tuples:
            if item != ev:
                new_list += [item]
        ten_tuples = new_list
        print(f"Remains in list: {ten_tuples}")
