
import random

def game(words):
    word_selection = random.choice(words)
    letters = {letter for letter in word_selection if letter != '\n'}
    list = []
    for number in enumerate(letters):
        pass
     
    
    print(word_selection)
    print(letters)
    #input('Enter a letter: ')


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