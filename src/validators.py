"""
Validates a user's guess

This module contains methods to validate the guess of a user. These include
methods to check the input is a string, and that it is five characters.

Typical Usage:

    >>> from src.validators import guess_is_string
    >>> guess_is_string('guess')
"""

from rich import print as rich_print

def guess_is_string(guess):
    """
    Checks that a guess is a string

    This method checks that a guess is a string. If not, an exception is
    raised.

    Args:
        guess -> Guess of a user
    
    Returns:
        None
    
    Raises:
        ValueError if guess is not a string
    """

    if not isinstance(guess, str):
        raise ValueError(f"{guess} should be a string")

def guess_is_five_characters(guess):
    """
    Checks that a guess is five characters

    This method checks that a guess is five characters. If it is not, an
    exception is raised. 

    Args:
        guess -> Guess of a user
    
    Returns:
        None
    
    Raises:
        ValueError if guess is not a string
    """

    if len(guess) != 5:
        raise ValueError(f"{guess} should be five characters")
