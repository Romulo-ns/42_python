#!/usr/bin/python3.10

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(3, 8)
    selected = random.sample(achievements, count)
    return set(selected)
        

def main() -> None:
    print("=== Achievement Tracker System ===")

    achievements = [
        "Fresh Meat", "First Blood", "The Journey Begins", "Awakening",
        "Apex Predator", "One Man Army", "Untouchable", "Raining Bullets",
        "Raining Blood", "David and Goliath", "No Stone Unturned",
        "Wanderlust", "Into the Abyss", "Off the Beaten Path",
        "Loot Goblin", "Midas Touch", "Dragon's Hoard", "Hoarder",
        "Task Failed Successfully", "What Does This Button Do?",
        "Gravity's Victim", "Leeroy Jenkins", "Godlike",
        "Against All Odds", "Perfectionist", "The 1%"
    ]

    players_name = [
        "Romulo",
        "Mafalda",
        "Victor",
        "Helena",
        "Guilherme",
        "Hugo",
        "Will"
    ]

    players = {}

    for player in players_name:
        players[player] = gen_player_achievements(achievements)

    print(players["Romulo"])
    x = players["Romulo"]
    print(len(x))


if __name__ == "__main__":
    main()
