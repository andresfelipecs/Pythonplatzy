
import random

def game(words):
    word_selection = random.choice(words)
    word_selection = "holaamigo"
    # create a lit comp for letter in word
    letters = [letter for letter in word_selection if letter != '\n']


    # ask the user to input a letter they want to guess from word
    list = letters[:]
    for i, n in enumerate(list):
        list[i] = "_"
    
    for i in range(3):        
    # replace letters with '_'
    
            single_letter = input(str('Please enter the letter to check: '))
        
    #compare single letter with all letters to match
            for index_val, elem in enumerate(letters):
                if single_letter == elem:
                    list[index_val] = elem
                    
                    
            #single_letter = input(str('Please enter the letter to check: '))
            print(list)


    # print(word_selection)
    # print(letters)
    


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