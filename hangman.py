import string
from words import choose_word
from images import IMAGES
from random import choice
'''
Important instruction
* function and variable name snake_case -> is_prime
* constant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    for letter in letters_guessed:
        secret_word = secret_word.replace(letter,"")
    
    if len(secret_word) == 0:
        return True

    return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase

    for letter in letters_guessed:
        letters_left = letters_left.replace(letter,"")
    return letters_left


def is_valid(letter, available_letters):

    if letter in available_letters and len(letter) == 1:
        return True
    return False
    



def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    remaining_lives = 8
    print("Lives remaining : {}".format(remaining_lives))
    letters_guessed = []
    hint_flag = False   
    
    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))

        guess = input("Please guess a letter or type 'hint' for getting a hint : ")
        
        if guess == "hint":
            if not hint_flag:
                hint_flag = True
                options = []
                for char in available_letters:
                    if char in secret_word:
                        options.append(char)
                guess = choice(options)
                print("Hint:",guess)
            else:
                print('You can only have the hint once in a game !\n')
                continue


        if not is_valid(guess, available_letters):
            print("Invalid Input ! Please try again..",end = '\n\n')
            continue

        letter = guess.lower()
        
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {}\n\n ".format(
                get_guessed_word(secret_word, letters_guessed)))
            
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            print(IMAGES[8-remaining_lives])
            remaining_lives -= 1
            print("Lives remaining : {}\n".format(remaining_lives))
            letters_guessed.append(letter)
            

    if remaining_lives == 0:
        print(" \n\n* * You lost. Better Luck Next Time. * * ")
        print("\nThe word is: {}".format(secret_word))


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)