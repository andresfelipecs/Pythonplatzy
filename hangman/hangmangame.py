
from hashlib import new
import random

def game(words):
    word_selection = random.choice(words)
    word_selection = "mongo"
    # create a lit comp for letter in word
    letters = [letter for letter in word_selection if letter != '\n']


    # ask the user to input a letter they want to guess from word
    single_letter = input(str('Please enter the letter to check: '))
    new_list = letters[:]
    

    # replace letters with '_'
    new_list = ['_' for i, _ in enumerate(new_list)]
    # for i, _ in enumerate(new_list):
    #     new_list[i] = "_"
        
    
    #compare single letter with all letters to match
    #new_list[i] = [ i for i, _ in enumerate(letters) if single_letter == i]
    for index_val, elem in enumerate(letters):
        if single_letter == elem:
            new_list[index_val] = elem


    print(word_selection)
    print(letters)
    print(new_list)
    


def read():
    words = []
    with open("./hangman/data.txt", "r", encoding = 'utf-8') as f: 
        for line in f:
            words.append(line)
    game(words)

def run():
    read()

if __name__ == '__main__':
    run()