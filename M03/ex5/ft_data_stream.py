#!/usr/bin/python3.10

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:

    players = ["alice", "bob", "charlie", "dylan"]

    actions = [
        "move",
        "jump",
        "run",
        "eat",
        "sleep",
        "grab",
        "release",
        "use"
    ]

    while True:
        player = random.choice(players)
        action = random.choice(actions)

        yield (player, action)


def consume_event(event_list: list[tuple[str, str]]
                  ) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield (event)


def main() -> None:
    print("=== Game Event Stream ===")

    event_generator = gen_event()

    for i in range(1000):
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = []
    for i in range(10):
        event = next(event_generator)
        event_list.append(event)
    print(event_list)

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list:: {event_list}")


if __name__ == "__main__":
    main()
