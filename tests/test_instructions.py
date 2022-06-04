"""
Unit tests for the instruction module

This module contains unit tests for the instructions module.

Typical Usage:
    pytest -v
"""

from tempfile import TemporaryDirectory
import os

import pytest

from src.instructions import generate_instructions_path
from src.instructions import check_instructions
from src.instructions import read_instructions


def test_generate_instructions_path():
    """
    Tests generate_instructions_path() method

    This method tests the generate_instructions_path() method

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    instructions_path = generate_instructions_path()
    assert isinstance(instructions_path, str)

def test_check_instructions():
    """
    Tests the check_instructions() method

    This method tests the check_instructions() method.

    Args:
        None
    
    Returns:
        None 
    
    Raises:
        None
    """

    home_directory = os.getcwd()
    with pytest.raises(FileNotFoundError):
        temp_dir = TemporaryDirectory()
        os.chdir(temp_dir.name)
        check_instructions()
        temp_dir.cleanup()
    
    os.chdir(home_directory)

def test_read_instructions():
    """
    Tests the read_instructions() method

    This method tests the read_instructions() method.

    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    instructions = read_instructions()
    assert isinstance(instructions, str)

def test_print_instructions(capfd):
    """
    Tests the print_instructions() method

    This method tests the print_instructions() method.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        None
    """

    console_output = capfd.readouterr()
    assert isinstance(console_output.out, str)
