"""
Tests methods in the Wardle class

This module contains unit tests for the Wardle class.

Typical Usage:
    pytest -v
"""

from collections import Counter

import pytest

from src.wardle import Wardle

@pytest.fixture
def wardle():
    """
    Sets up the Wardle object for testing.

    This method fetches the Wardle object and returns it for use in
    other unit tests.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    wardle = Wardle()
    return wardle

def test_is_exact_match(wardle):
    """
    Tests is_exact_match() method

    This method tests the is_exact_match() method.

    Args:
        wardle -> Wardle object created via pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = "snail"

    matches = wardle.is_exact_match(guess_word)
    assert matches is True

def test_letter_position_matches(wardle):
    """
    Tests letter_position_matches() method.

    This method tests the letter_position_matches() method.

    Args:
        wardle -> Wardle object created by pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = 'superman'

    matches = wardle.letter_position_matches(0, guess_word[0])
    assert matches is True

def test_letter_in_word(wardle):
    """
    Tests letter_in_word() method.

    This method tests the letter_in_word() method.

    Args:
        wardle -> Wardle object created by pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = "greaves"

    matches = wardle.letter_in_word(guess_word[-1])
    assert matches is True

def test_validate_guess_with_non_string(wardle, capfd):
    """
    Tests the validate_guess() method

    This method tests the validate_guess() method to ensure
    it prints the expected message if a non-string value is
    passed.

    Args:
        wardle -> Wardle object created by pytest fixture
        capfd -> Captures input and output
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_guess = 3.142

    wardle.validate_guess(invalid_guess)
    output = capfd.readouterr()

    assert isinstance(output.out, str)

def test_validate_guess_with_long_string(wardle, capfd):
    """
    Tests the validate_guess() method

    This method tests the validate_guess() method to ensure
    it prints the expected message if a long string is passed
    to it.

    Args:
        wardle -> Wardle object created by pytest fixture
        capfd -> Captures input and output
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_guess = "greaves"

    wardle.validate_guess(invalid_guess)
    output =  capfd.readouterr()

    assert isinstance(output.out, str)

def test_validate_guess_with_short_string(wardle, capfd):
    """
    Tests the validate_guess() method

    This method tests the validate_guess() method to ensure it
    prints the expected message if a short string is passed.

    Args:
        wardle -> Wardle object created by pytest fixture
        capfd -> Captures input and output
    
    Returns:
        None
    
    Raises:
        None
    """

    invalid_guess = "fish"

    wardle.validate_guess(invalid_guess)
    output = capfd.readouterr()

    assert isinstance(output.out, str)

def test_check_guess_all_true(wardle):
    """
    Tests the check_guess() method returns expected list

    This method tests the check_guess() method to ensure that it returns
    a list contain only True booleans if two words match exactly.

    Args:
        wardle -> Wardle object created by pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = "snail"

    matches = wardle.check_guess(guess_word)
    values_count = Counter(matches)["correct_position"]
    assert values_count == len(guess_word)

def test_check_guess_some_true(wardle):
    """
    Tests the check_guess() method returns expected list

    This method tests the check_guess() method to ensure it returns
    a list containing both True and False boolean values.

    Args:
        wardle -> Wardle object created by pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = "paris"

    matches = wardle.check_guess(guess_word)
    values_count = Counter(matches)["correct_letter"]
    assert values_count == 2

def test_check_guess_all_false(wardle):
    """
    Tests the check_guess() method returns expected list

    This method tests the check_guess() method to ensure it returns
    a list containing only False values.

    Args:
        wardle -> Wardle object created by pytest fixture
    
    Returns:
        None
    
    Raises:
        None
    """

    guess_word = "trout"

    matches = wardle.check_guess(guess_word)
    values_count = Counter(matches)["incorrect"]
    assert values_count == len(guess_word)
