"""
Displays game results to the console

This module contains various methods to display the results of the Wardle 
game to the console.

Typical Usage:
    >>> from src.display import create_display_string
    >>> create_display_string
"""

from rich import print as rich_print
from rich.prompt import Prompt

def ask_for_user_guess():
    """
    Asks the user for their guess

    This method asks the user to input their guess. It returns the
    guess for further use in the program.

    Args:
        None
    
    Returns:
        user guess -> Word input by the user
    
    Raises:
        None
    """

    question = "\n[cyan]Enter your guess [/]"
    guess_word = Prompt.ask(question)

    return guess_word

def create_display_string(guess: str, results: list) -> str:
    """
    Creates a display string for Rich̀

    This method creates a display string, containing the appropriate
    syntax to print the results of the game to the console. It takes
    the results of the game, which should be a list. It then iterates
    through these and constructs a string to be printed to the console.

    Args:
        results -> Results of the game
    
    Returns:
        String containing formatting instructions for Rich
    
    Raises:
        None
    """

    display_list = []
    
    for letter, result in zip(guess, results):
        if result == "correct_position":
            display_list.append(f"[black on green]{letter}")
        elif result == "correct_letter":
            display_list.append(f"[black on yellow]{letter}")
        elif result == "incorrect":
            display_list.append(f"[black on red]{letter}")
        else:
            raise ValueError(f"Unexpected result received: {result}")
    
    display_list.append("[/]")
    
    display_string = "".join(display_list)
    return display_string


def print_display_string(display_string: str):
    """
    Prints a display string to the console

    Takes a formatted display string and prints it to the console, using the
    Rich library to translate the formatting into various coloured boxed.

    Args:
        display_string -> Display string to print
    
    Returns: 
        None
    
    Raises:
        None
    """

    rich_print(display_string)


def print_exact_match():
    """
    Informs the user of an exact match

    This method informs the user that they have achieved an exact match,
    by printing green text to the console along with an emoji.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    rich_print("[green on black]Congrats! That's an exact match :clap:[/]")


def print_no_more_attempts():
    """
    Informs the user they have no more attempts

    This method informs the user that they have reached their limit of 
    attempts. It displays a message in red to that effect.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    rich_print("[red on black]Bad luck - you're out of attempts. Better luck next time![/]")
