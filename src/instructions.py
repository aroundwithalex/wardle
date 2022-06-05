"""
Contains instructions on how to play the game.

This module prints instructions on how to play the game to the console. 
It provides an indication of what the different statuses mean and how many
attempts a user has.

Typical Usage:
    >>> from instructions import instruct
    >>> instruct()
"""

from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown

def generate_instructions_path():
    """
    Generates path to instructions file

    This method generates the path to the instructions file, so it can be
    read and displayed on the console.

    Args:
        None
    
    Returns:
        Path to instructions
    
    Raises:
        None
    """

    make_instructions_path = f"{Path.cwd()}/data/instructions.md"
    return make_instructions_path

def check_instructions():
    """
    Checks instructions exist at expected path.

    This method ensures that the instructions exist at the expected path. If
    they don't an exception is raised.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        FileNotFoundError if instructions don't exist
    """

    instructions_path = generate_instructions_path()
    if not Path(instructions_path).exists():
        raise FileNotFoundError(f"{instructions_path} does not exist.")

def read_instructions():
    """
    Reads instructions from file.

    This method reads instructions from a specific file. It returns them, so
    they can be printed to the console

    Args: 
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    check_instructions()

    instructions_path = generate_instructions_path()
    with open(instructions_path, 'r', encoding='utf-8-sig') as instructions:
        markdown = Markdown(instructions.read())
        return markdown

def print_instructions():
    """
    Generates instructions to the console.

    This method generates instructions to the console to tell the user
    how to play the Wordle game.

    Arguments:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    instructions = read_instructions()

    console = Console()
    console.print(instructions)
