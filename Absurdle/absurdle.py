from colorama import Back
from random import choice
import sys
# For test purposes, do not change these imports.
# You can add more below this line if needed.

#Dictionary COLOR_MAP
# Each letter represetns a result
COLOR_MAP = {'G': Back.GREEN, 'Y': Back.YELLOW, 'W': Back.WHITE}

#DO NOT CHANGE
def show_result(result, guess):
    # Display the result using the colorama library
    for i in range(len(result)):
        print(COLOR_MAP[result[i]] + guess[i], end='')
    print(Back.RESET)

#DO NOT CHANGE
def load_five_letter_words(filename):
    with open(filename, 'r') as f:
        # Strip out spaces, convert words to uppercase, filter to only 5-letter words
        return [word.strip().upper() for word in f if len(word.strip().upper()) == 5]


def get_result(secret_word, guess):
    # Initially, label every letter W by default
    result = ['W' for _ in range(5)]

    #Change: Added list to be able to modify the strings
    #This way, I am able to remove letters once they are used (prevent duplicates)
    secret_letters = list(secret_word)
    guess_letters = list(guess)

    # Check for correct letters first
    for i in range(len(guess)):
        # Right position
        if guess_letters[i] == secret_letters[i]:
            result[i] = 'G'

            #Change: Remove used letter
            secret_letters[i] = None
            guess_letters[i] = None
            
    # Wrong position but in word somewhere
    #Instead of just checking, mark yellows
    for i in range(len(guess)):

        #Now check if the guessed letter still exists in unused secret letters
        if guess_letters[i] is not None and guess_letters[i] in secret_letters:
            result[i] = 'Y'
            #Find index of the first occurence of the letter and set to 'NONE'
            secret_letters[secret_letters.index(guess_letters[i])] = None
            guess_letters[i] = None


    return ''.join(result)


def is_valid_guess(guess, five_letter_words):
    # The guess must be a valid 5-letter word
    correct_length = len(guess) == 5
    only_letters = guess.isalpha()
    
    existing_word = False

    if guess in five_letter_words:
        existing_word = True

    return correct_length and only_letters and existing_word


def get_guess(words):
    guess = input('Enter a 5-letter guess: ').strip().upper()

    # Keep asking the user to try again until they enter a valid guess
    while not is_valid_guess(guess,words):
        guess = input('Guess must be a valid word consisting of 5 letters, try again: ').strip().upper()
    return guess

def get_adversarial_result(guess, remaining_words):
    """

    This function gets the adversarial result of a guess.


    """

    pattern_groups = {}

    #Group words by their result pattern
    for word in remaining_words:
        result = get_result(word, guess)

        if result not in pattern_groups:
            pattern_groups[result] = []

        pattern_groups[result].append(word)

    #Worst Pattern
    largest_pattern = max(pattern_groups, key = lambda pattern:( len(pattern_groups[pattern]),
                                                                -pattern.count('G'),
                                                                -pattern.count('Y'),
                                                                pattern
                                                                )
                                                            )
    #Keep only the largest group
    new_remaining_words = pattern_groups[largest_pattern]

    return largest_pattern, new_remaining_words



    

def main():


    if len(sys.argv) != 2:
       print('Usage: python wordle.py <word_list_file>')
       return
    words_file = sys.argv[1]
    # Load a list of valid five letter words from a file
    five_letter_words = load_five_letter_words(words_file)
    # Randomly select a secret word from the list
    #secret_word = choice(five_letter_words)
    #print(secret_word)
    #secret_word = "RACER"
    result = 'WWWWW'
    # While the user hasn't won yet

    remaining_words = five_letter_words
    while result != 'GGGGG':
        # Ask the user to guess
        guess = get_guess(five_letter_words)
       # Determine what the result string should be, e.g. WYGGY
        result, remaining_words = get_adversarial_result(guess, remaining_words)
   
       # Display the guess using the colors from the result string
        show_result(result, guess)
    print('You win!')


if __name__ == '__main__':
    main()


