"""
Unit tests for validator methods

This module contains unit tests for the validator methods.

Typical Usage:
    pytest -v
"""

import pytest

from src.validators import (guess_is_string,
                            guess_is_five_characters)


def test_guess_is_string_raises_exception(): 
    """
    Tests guess_is_string() raises Exception

    This method tests the guess_is_string() method to ensure it raises an
    exception as expected.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    with pytest.raises(ValueError):
        guess_is_string(3.142)

def test_guess_is_five_characters():
    """
    Tests guess_is_five_characters() raises Exception

    This method tests guess_is_five_characters() raises an Exception if a
    string longer than five characters is passed to it.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    with pytest.raises(ValueError):
        guess_is_five_characters("greaves")
