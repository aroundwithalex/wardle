"""
Main module for Wardle game

This module contains the main method for the Wardle game. It enables the
game to be played to aggregating all the different classes and methods,
including those to print the instructions the console, those to play the
game and those to display the results.

Typical Usage:
    $ ./main.py
"""

from src.instructions import print_instructions

from src.wardle import Wardle

from src.display import (create_display_string,
                         print_display_string,
                         print_no_more_attempts,
                         print_exact_match)

def main():
    """
    Main method for the Wardle game.

    This method represents the main method for the Wardle game. It contains all
    the classes and methods required to start a game, and initialises a while
    loop to enable a user to keep guessing until they run out of attempts.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    wardle = Wardle()
    print_instructions()

    attempts = 6
    while attempts >= 0:
        guess_word = input("Enter your guess: ")

        is_valid = wardle.validate_guess(guess_word)
        if not is_valid:
            attempts -= 1
            continue

        if wardle.is_exact_match(guess_word):
            print_exact_match()
            break

        if attempts == 0:
            print_no_more_attempts()
            break

        results = wardle.check_guess(guess_word)
        result_string = create_display_string(guess_word, results)
        print_display_string(result_string)
        attempts -= 1

if __name__ == '__main__':
    main()
