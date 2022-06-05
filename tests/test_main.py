"""
Unit tests for the main module

This module contains unit tests for the main module.

Typical Usage:
    pytest -v
"""

from main import main

def test_main_with_non_string_guess(capfd, monkeypatch):
    """
    Tests main with invalid guess

    This method tests the main method with an invalid guess.

    Args:
        capfd -> Captures the command line input
    
    Returns:
        None
    
    Raises:
        None
    """

    guesses = [
        "paris",
        "trout",
        3.142,
        "kevin",
        "hedge",
        "lamps"
    ]

    output_messages = []

    for word in guesses:
        monkeypatch.setattr("rich.prompt.Prompt.ask", lambda guess: word)
        main()
        output = capfd.readouterr()
        output_messages.append(output.out)

    non_string_message = output_messages[2]
    assert isinstance(non_string_message, str)

def test_main_with_long_guess(capfd, monkeypatch):
    """
    Tests with guess longer than five characters

    This method tests the main method with a guess longer than five
    characters. It checks to see whether an error message is raised.

    Args:
        capfd -> Captures input and output
        monkeypatch -> Patches builtins.input
    
    Returns:
        None
    
    Raises:
        None
    """

    guesses = [
        "paris",
        "trout",
        "greaves",
        "lemar",
        "warne",
        "jones"
    ]

    output_messages = []
    for word in guesses:
        monkeypatch.setattr("rich.prompt.Prompt.ask", lambda guess: word)
        main()
        output = capfd.readouterr()
        output_messages.append(output.out)
    
    long_string_message = output_messages[2]
    assert isinstance(long_string_message, str)

def test_main_with_short_guess(capfd, monkeypatch):
    """
    Tests with guess shorter than five characters

    This method tests the main method with a guess containing less than
    five characters. It checks to see whether an error message is raised.

    Args:
        capfd -> Capture input and output
        monkeypatch -> Patches builtins.input
    
    Returns:
        None
    
    Raises:
        None
    """

    guesses = [
        "paris",
        "trout",
        "blue",
        "lemar",
        "thing",
        "leeds"
    ]

    output_messages = []
    for word in guesses:
        monkeypatch.setattr("rich.prompt.Prompt.ask", lambda guess: word)
        main()
        output = capfd.readouterr()
        output_messages.append(output.out)
    
    short_string_message = output_messages[2]
    assert isinstance(short_string_message, str)

def test_main_with_correct_guess(capfd, monkeypatch):
    """
    Tests with correct first time guess

    This method tests the main method with a correct first time
    guess.

    Args:
        capfd -> Captures the command line output
        monkeypatch -> Patches builtins.input
    
    Returns:
        None
    
    Raises:
        None
    """

    monkeypatch.setattr("rich.prompt.Prompt.ask", lambda word:"snail")
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
        monkeypatch.setattr("rich.prompt.Prompt.ask", lambda guess: word)
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
        monkeypatch.setattr("rich.prompt.Prompt.ask", lambda guess: word)
        main()
        output = capfd.readouterr()
    
    assert isinstance(output.out, str)
