"""
Current tennis score displayer

Usage:
1. Display current score:
   python main.py 3-5
   python main.py 3-5 --names Serena Naomi

2. Display scores from a file:
   python main.py scores.txt
   python main.py scores.txt --names Djokovic Nadal

"""

import argparse
from enum import Enum


class Score(Enum):
    """
    Enum to represent the standard tennis scores.
    """
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3


class TennisScore:
    """
    Class to display the current score during a tennis game.
    """

    WINNING_SCORE = 4

    def __init__(self, first_player="Player 1", second_player="Player 2"):
        """
        Constructor that initializes a TennisScore instance
        with default player names and scores.

        Args:
            first_player (str): Name of the first player, default value "Player 1"
            second_player (str): Name of the second player, default value "Player 2"
        """
        self.player1_name = first_player
        self.player2_name = second_player
        self.player1_score = 0
        self.player2_score = 0

    def is_deuce(self):
        """
        Check if the current score is a deuce.
        If at least three points have been scored by each player,
        and the scores are equal, the score is Deuce.

        Returns:
            bool: True if the score is a deuce, False otherwise.
        """
        return self.player1_score >= 3 and self.player1_score == self.player2_score

    def is_advantage(self):
        """
        Check if one player has an advantage.
        If at least three points have been scored by each player,
        and one player has one more point than its opponent,
        the score is Advantage for that player.

        Returns:
            bool: True if one player has an advantage, False otherwise.
        """
        return (
                self.player1_score >= self.WINNING_SCORE or self.player2_score >= self.WINNING_SCORE
        ) and abs(self.player1_score - self.player2_score) == 1

    def is_win(self):
        """
        Check if one player has won the game.
        A game is won by the first player to have won at least four points,
        and at least two points more than its opponent.

        Returns:
            bool: True if one player has won, False otherwise.
        """

        if max(self.player1_score, self.player2_score) == self.WINNING_SCORE:
            return True
        return (
                max(self.player1_score, self.player2_score) >= self.WINNING_SCORE
                and abs(self.player1_score - self.player2_score) == 2
            )

    def current_score(self):
        """
        Calculate the current score based on the game rules.

        Returns:
            str: A string representation of the current score.
        """
        # check deuce
        if self.is_deuce():
            return "Deuce"

        # check advantage
        if self.is_advantage():
            leader = self.player1_name \
                if self.player1_score > self.player2_score else self.player2_name
            return f"Advantage for {leader}"

        # check win
        if self.is_win():
            winner = self.player1_name \
                if self.player1_score > self.player2_score else self.player2_name
            return f"Win for {winner}"

        # for 0-3 return point names
        if self.player1_score < self.WINNING_SCORE and self.player2_score < self.WINNING_SCORE:
            if self.player1_score == self.player2_score:
                return f"{Score(self.player1_score).name.capitalize()}-All"
            return f"{Score(self.player1_score).name.capitalize()}-" \
                f"{Score(self.player2_score).name.capitalize()}"

        # if nothing was valid up until this point then score is invalid such as 1-5, 6-9
        return "Invalid Score"


def process_file(file_path, p1_name, p2_name):
    """
       Reads and process a list of score inputs from the file and print the results  line by line.
       """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        display = TennisScore(p1_name, p2_name)
        for line in lines:
            try:
                p1_score, p2_score = map(int, line.strip().split('-'))
                display.player1_score = p1_score
                display.player2_score = p2_score
                print(f"{line.strip()} -> {display.current_score()}")
            except ValueError:
                print(f"Invalid input: {line.strip()}, Please provide scores in the format 'X-Y'")
    except FileNotFoundError:
        print(f"File not found: {file_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Display the current score during a tennis game")
    parser.add_argument("input", help="Current score in 'X-Y' format (e.g., '3-2') or a file path.")
    parser.add_argument("--names", nargs=2, metavar=("PLAYER1", "PLAYER2"),
                        help="Optional player names (e.g., 'Djokovic Nadal').")

    args = parser.parse_args()

    # if no names provided, default is Player 1 - Player 2
    player1_name, player2_name = args.names if args.names else ("Player 1", "Player 2")

    if args.input.endswith(".txt"):
        process_file(args.input, player1_name, player2_name)
    else:
        try:
            player1_score, player2_score = map(int, args.input.split('-'))
            game = TennisScore(player1_name, player2_name)
            game.player1_score = player1_score
            game.player2_score = player2_score
            print(f"Current Score: {game.current_score()}")
        except ValueError:
            print("Invalid input. Please provide scores in the format 'X-Y' or a valid file path.")
