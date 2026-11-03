#!/usr/bin/python3.10

import random


def gen_player_achievements(achievements: list[str]) -> set[str]:
    count = random.randint(3, 8)
    selected = random.sample(achievements, count)
    return set(selected)


def print_players_achievements(players: dict) -> None:
    for player, achivements in players.items():
        print(f"Player {player}: {achivements}")


def all_distinct_achievements(players: dict) -> set[str]:
    all_achievements: set[str] = set()

    for player in players.values():
        all_achievements = all_achievements.union(player)

    return all_achievements


def common_achievements(players: dict) -> set[str]:
    common: set[str] = set()
    first_player = True

    for player in players.values():
        if first_player:
            common = player
            first_player = False
        else:
            common = common.intersection(player)

    return common


def unique_achievements(players: dict) -> dict:
    unique_players = {}

    for player_name, achievements in players.items():
        other_achievements: set[str] = set()

        for other_name, other_set in players.items():
            if other_name != player_name:
                other_achievements = other_achievements.union(other_set)

        unique = achievements.difference(other_achievements)

        unique_players[player_name] = unique

    return unique_players


def missing_achievements(players: dict, achievements: list[str]) -> dict:
    missing_players = {}
    all_achievements = set(achievements)

    for player_name, player_achi in players.items():
        missing_players[player_name] = player_achi.difference(all_achievements)

    return missing_players


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

    print_players_achievements(players)

    all_achievements = all_distinct_achievements(players)
    print(f"\nAll distinct achievements: {all_achievements}")

    common = common_achievements(players)
    if len(common) > 0:
        print(f"\nCommon achievements: {common}")
    else:
        print("\nNo common achievements\n")

    unique = unique_achievements(players)
    for player, achievements in unique.items():
        if len(achievements) > 0:
            print(f"Only {player} has: {achievements}")
        else:
            print(f"{player} has: no unique achievements")

    print("\n")
    missing = missing_achievements(players, achievements)
    for player, achievements in missing.items():
        print(f"{player} is missing: {achievements}")


if __name__ == "__main__":
    main()
