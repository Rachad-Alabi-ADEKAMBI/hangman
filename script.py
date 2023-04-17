import random
import string
from words import words


def get_random_word_without_space_or_underscore(words):
    """
    Returns a random word from the list of words, excluding those that contain
    spaces or underscores.
    """
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_random_word_without_space_or_underscore(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Display information to the user
        print(
            f"You have {lives} lives left and you have used these letters: {' '.join(used_letters)}")

        # Show the word with hidden letters
        word_list = [
            letter if letter in used_letters else '_' for letter in word]
        print(f"Current word: {' '.join(word_list)}")

        # Get user input
        user_letter = input('Guess a letter: ').upper()

        # Validate user input
        if len(user_letter) != 1 or user_letter not in alphabet:
            print('Invalid character, please try again')
            continue
        elif user_letter in used_letters:
            print('You have already used that character, please try again')
            continue

        # Check if user guessed a correct letter
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            lives -= 1
            print('Letter is not in the word.')

    # Show the result
    if lives == 0:
        print(f"Sorry, you died, the word was {word}")
    else:
        print(f"You guessed the word '{word}'!!")


hangman()
