# Write a program that prompts the user to guess a hidden word, one letter at a time. 
# The program should display the current state of the word (e.g., “_ _ _ _ _”) 
# and the letters the user has already guessed.

import random

def hangman():
    """
    Play a game of Hangman.
    """

    # Define a list of words to choose from
    words = ['cloud', 'python', 'program', 'hangman', 'computer', 'science', 'funineering', 'technology']

    # Select a random word from the list
    word = random.choice(words)

    # Initialize the game state
    guesses = ''
    turns = 6

    # Loop until the game is over
    while turns > 0:
        # Print the current state of the word
        display_word = ''
        for letter in word:
            if letter in guesses:
                display_word += letter
            else:
                display_word += '_ '
        print(display_word)

        # Prompt the user to guess a letter
        guess = input('Guess a letter: ').lower()

        # Check if the letter has already been guessed
        if guess in guesses:
            print('You already guessed that letter!')

        # Check if the letter is in the word
        elif guess in word:
            print('Good guess!')
            guesses += guess

        # If the letter is not in the word
        else:
            print('Oops, that letter is not in the word.')
            turns -= 1

        # Check if the user has guessed all the letters in the word
        if all(letter in guesses for letter in word):
            print('Congratulations, you guessed the word!')
            return

    # If the user runs out of turns
    print('Sorry, you ran out of turns. The word was', word)

# Example usage:
hangman()
