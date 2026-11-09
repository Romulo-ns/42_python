#!/usr/bin/python3.10

import random

def main() -> None:
    print("=== Game Data Alchemist ===\n")

    players = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam"
    ]

    print(f"Initial list of players: {players}")

    capitalized_players = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    original_capital = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {original_capital}\n")

    score_dict = {
        player: random.randint(0, 100) for player in capitalized_players
        }
    print(f"Score dict: {score_dict}")

    score_average = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {score_average:.2f}")

    high_scores = {
        player: score for player, score in score_dict.items() 
        if score > score_average
        }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
