"""
Enables a user to play Wardle.

This module contains the methods required to enable a user to play Wardle. It
fetches a hidden word and asks a user for their input.  It then checks that
input to ensure the given letter occurs in the word, and outputs the result to
the user.

Typical Usage:
    >>> from src.wardle import play_wardle
    >>> play_wardle()
"""

class Wardle():
    """
    Sets parameters for Wardle, and launches game.

    This class sets the parameters for the Wardle game, and enables a user
    to start a new game. It sets the number of attempts and sets a hidden
    word. It then enables the user to check their output against the word
    and returns their status throughout the game.

    Attributes:
        attempts -> Sets the number of attempts a user has
    """

    def __init__(self):
        """
        Constructor for Wardle class.

        This constructor initialises only one instance variable: to set the number
        of attempts a user has to play the game.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """
        
        self.hidden_word = "snail"
    
    def is_exact_match(self, guess):
        """
        Checks a hidden word and a guess

        This method checks to see whether a hidden word exactly matches
        a guess. If it does, the method returns True; otherwise False.

        Args:
            hidden_word -> Hidden word to match
            guess -> Guess to match the hidden word against
        
        Returns:
            True if letter in right place
            False otherwise
        
        Raises:
            None
        """

        return self.hidden_word == guess
    
    def letter_position_matches(self, index, letter):
        """
        Checks if letter is in right place

        This method checks to see if a letter is in the right position
        in the hidden word. It returns True if so; False otherwise.

        Args:
            hidden_word -> Hidden word to match
            letter -> Letter to place within hidden word
        
        Returns:
            List containing letter position matches
        
        Raises:
            None
        """

        return self.hidden_word[index] == letter

    def letter_in_word(self, letter):
        """
        Finds shared letters between hidden word and guess

        This method finds shared letters between the hidden word and the
        guess. It returns a list of these matches, where the letter is in
        the word but not necessarily in the right place.

        Args:
            hidden_word -> Hidden word to check
            guess -> user guess to compare against hidden word
        
        Returns:
            List containing boolean values, indicating if the letter is in the word
        
        Raises:
            None
        """

        return letter in self.hidden_word
    
    def check_guess(self, guess):
        """
        Checks guess against hidden word

        This method checks to see whether a guess is within a hidden word. If 
        so, it returns an array indicating how many letters are in the right 
        position. Otherwise it returns an array indicating how many are out of 
        order, or don't exist in the word.

        Args: 
            guess -> Guess to compare against hidden word
        
        Returns:
            Array indicating how many are in correct position
        
        Raises:
            None
        """

        matches_found = []

        for index, letter in enumerate(guess):
            if self.letter_position_matches(index, letter):
                matches_found.append("correct_position")
            elif self.letter_in_word(letter):
                matches_found.append("correct_letter")
            else:
                matches_found.append("incorrect")
        
        return matches_found
