#!/usr/bin/python3.10

import sys


def no_scores_provided_error_msg() -> None:
    print(f"No scores provided. Usage: {sys.argv[0]} <score1> <score2> ...")


def score_analytics() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)

    if argc == 1:
        no_scores_provided_error_msg()
    else:
        scores = []
        for i in sys.argv[1:]:
            try:
                scores.append(int(i))
            except ValueError:
                print(f"Invalid parameter: '{i}'")

        if len(scores) == 0:
            no_scores_provided_error_msg()
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {argc - 1}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {(sum(scores)/ len(scores)):.1f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


def main() -> None:
    score_analytics()


if __name__ == "__main__":
    main()
