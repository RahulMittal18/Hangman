import random


def load_words():
    """
    this function help to load more words by updating word_list (list)    
    """   
    inFile = open("words.txt", "r")
    line = inFile.read()
    word_list = line.split()

    return word_list


def choose_word():
    """
    word_list (list): list of words (strings)
    this function return one random word from list
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
