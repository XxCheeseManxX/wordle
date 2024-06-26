from config import settings
import helper

num_guesses = helper.get_guesses()

answer = helper.get_word()

# Initialize an empty list that stores the guessed words (can't guess a word more than once)
guessed_words = list()

# Guessed words with the reminal coloring applied
guessed_words_colored = list()

# User can guess until num_guesses == 0. Subtract 1 from num_guesses after each guess
while num_guesses > 0:
    print("\n")
    # All the words in text files are lowercase
    guess = input("Guess: ").lower()

    # Check if word has already been guessed
    if guess in guessed_words:
        print("Word already guessed")
        continue
    guessed_words.append(guess)

    #Checks if the guess is legal
    if not helper.check_allowed(guess):
        print("Not an allowed word!")
        continue
    
    # Compare guessed word to the answer!
    if guess == answer:
        print("You win!")
        """
        Adds the answer to guessed words so we can 
        check to see if we should print loser message
        """
        guessed_words.append(answer)
        print(helper.print_guess_result(guessed_words_colored, guess, answer))
        break
    
    print(helper.print_guess_result(guessed_words_colored, guess, answer))
        
    num_guesses -= 1

# If the answer was not found we print this
if answer not in guessed_words:
    print(f"Out of tries! Answer was {answer}")

