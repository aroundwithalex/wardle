"""
Unit tests for the WardleDisplay class

This module contains unit tests for the WardleDisplay class.

Typical Usage:
    pytest -v
"""

from src.display import create_display_string
from src.display import print_display_string
from src.display import print_exact_match
from src.display import print_no_more_attempts

def test_create_display_string():
    """
    Tests the create_display_string() method.

    This method tests the create_display_string() method.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    guess = "snail"
    results = [
        "correct_position",
        "correct_position",
        "correct_position",
        "correct_position",
        "correct_position"
    ]

    display_string = create_display_string(guess, results)
    assert isinstance(display_string, str)

def test_print_display_string(capfd):
    """
    Tests the print_display_string() method

    This method tests the print_display_string() method.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """

    guess = "paris"
    results = [
        "incorrect",
        "correct_letter",
        "incorrect",
        "correct_letter",
        "correct_letter"
    ]

    display_string = create_display_string(guess, results)
    print_display_string(display_string)

    output = capfd.readouterr()
    assert isinstance(output.out, str)

def test_print_exact_match(capfd):
    """
    Tests print_exact_match() method

    This method tests the print_exact_match() method

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    print_exact_match()
    output = capfd.readouterr()

    assert isinstance(output.out, str)

def test_print_no_more_attempts(capfd):
    """
    Tests print_no_more_attempts() method

    This method tests the print_no_more_atempts() method.

    Args:
        None
    
    Returns: 
        None
    
    Raises:
        None
    """

    print_no_more_attempts()
    output =  capfd.readouterr()

    assert isinstance(output.out, str)
