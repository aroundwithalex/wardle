# Wardle

## What is Wardle?

Wardle is a text-based game, based on Wordle of the New York times. The aim
of the game is to guess a five character word in fewer than six attempts.

## How do I use Wardle?

First, clone this Git repo and `cd` into the source directory. Type `python3 ./main.py`, and a set of instructions should appear along with a prompt, asking you for your first guess.

If you guess correctly at any point, you'll receive a message similar to the following: -

`Congrats! That's an exact match`

Otherwise, your guess will be output with different boxes indicating the accuracy of each letter. The key is: -

- Green -> the letter is in the word, and in the correct position.
- Yellow -> the letter is in the word, but in a different position.
- Grey -> the letter is not in the word.

After six attempts, the following message will be output: -

`Bad luck - you're out of attempts. Better luck next time!`

## How do I run the associated unit tests?

To run the associated unit tests, create a virtual environment within the host directory and install the `pytest` package. You can then use the following command to run all unit tests: -

`pytest -v`
