"""
Unit tests for the main module

This module contains unit tests for the main module.

Typical Usage:
    pytest -v
"""

from main import main

def test_main_with_correct_guess(capfd, monkeypatch):
    """
    Tests with correct first time guess

    This method tests the main method with a correct first time
    guess.

    Args:
        capfd -> Captures the command line output
    
    Returns:
        None
    
    Raises:
        None
    """

    monkeypatch.setattr("builtins.input", lambda word:"snail")
    main()
    output = capfd.readouterr()

    assert isinstance(output.out, str)

def test_main_with_eventual_correct_answer(capfd, monkeypatch):
    """
    Tests main with an eventually correct answer

    This method tests the main() method with multiple values, one of
    which will eventually be correct.

    Args:
        capfd -> Captures standard output
        monkeypatch -> Patches builtins.input
    
    Returns:
        None
    
    Raises:
        None
    """

    words = ["lemar", "paris", "snail"]

    for word in words:
        monkeypatch.setattr("builtins.input", lambda guess: word)
        main()
        output = capfd.readouterr()
    
    assert isinstance(output.out, str)

def test_main_with_no_more_attempts(capfd, monkeypatch):
    """
    Tests main until no more attempts raised

    This method tests the main method until the user runs out of attempts. By
    default, this is set to six.

    Args:
        capfd -> Captures standard output
        monkeypatch -> Patches builtins.input
    
    Returns:
        None
    
    Raises:
        None
    """

    words = [
        "lemar", 
        "paris",
        "lorem",
        "ipsus",
        "ipsum",
        "dolor"
    ]

    for word in words:
        monkeypatch.setattr("builtins.input", lambda guess: word)
        main()
        output = capfd.readouterr()
    
    assert isinstance(output.out, str)
