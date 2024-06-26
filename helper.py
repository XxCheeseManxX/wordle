from config import settings
import random
from termcolor import colored

def get_guesses():
    """
    Gets the number of guesses the user wants to play with
    If not specified, default is applied from config.py(official wordle uses 6 guesses)

    Will loop in while loop until a valid number is input
    """
    while True:
        num_guesses = input(f"Number of guesses(default {settings['default_guesses']}): ")
        # if not checks for: None, False, 0, empty string/list/whatever
        if not num_guesses:
            num_guesses = settings['default_guesses']
        if not str(num_guesses).isdigit():
            print("Invalid input. Please enter a number")
            print("\n")
            continue
        return int(num_guesses)

def get_word():
    """
    Gets a random word from the wordle-answers.txt file (will be the answer)
    
    Opens the text file, store all the words in a list. 
    random.choice chooses a word at random from the list
    """
    with open("wordle-answers.txt", "r") as file:
        words = [line.strip() for line in file.readlines()]
    return random.choice(words)

def check_allowed(guess):
    """
    Check if guessed word is in the allowed words text file
    """
    with open("allowed-words.txt", "r") as file:
        allowed_words = [line.strip() for line in file.readlines()]
    if guess in allowed_words:
        return True
    return False

def print_guess_result(guessed_words_colored, guess, answer):
    """
    Compares the guess to the answer and applied the color coding using 
    termcolor

    Also prints the prior guessed words
    """
    for word in guessed_words_colored:
        print(word)

    result = ""

    # Check the # of occurences of green for each letter in a guess
    matched = {}
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            if guess[i] in matched:
                matched[guess[i]] += 1
            else:
                matched[guess[i]] = 1


    for i in range(len(guess)):
        # Check for green
        if guess[i] == answer[i]:
            result += colored(guess[i], settings['letter_correct'])
        # Check for yellow
        
        #If all green letters guessed correctly, we make another of the same
        #letter grey. If not, it is yellow
        #Ex: Word is "vigor". If we guess "rigor", the first r should be grey!(all r guessed)
        #Ex2: Word is "sassy". If we guess "press", the last s should be yellow 
        #(Not all s are guessed)

        elif guess[i] in answer:
            # We check to see how many green letters are in the guess
            if guess[i] in matched:
                # If there are less green letters in the guess that that letter 
                #in the answer, letter is yellow
                if matched[guess[i]] < answer.count(guess[i]):
                    result += colored(guess[i], settings['letter_in_word'])
                # Else, we have gotten all the locations of that letter (all greens). 
                #We grey it out
                else:
                    result += colored(guess[i], settings['letter_incorrect'])
            # This means there are no green occurences of this letter, make it yellow
            else:
                result += colored(guess[i], settings['letter_in_word'])
        # Else, light gray
        else:
            result += colored(guess[i], settings['letter_incorrect'])\
    # List to print the prior guesses with their colors
    guessed_words_colored.append(result)
    return result
