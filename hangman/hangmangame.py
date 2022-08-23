
import random

def game(words):
    word_selection = random.choice(words)
    letters = [letter for letter in word_selection if letter != '\n']
    single_letter = input(str('Please enter the letter to check: '))
    list = ['_' for i in enumerate(letters)]
    #print(list)
    
    if single_letter in letters:
        list2 = [single_letter]
        new_list = [element for element in letters if element in list2]
        print(list)
    else:
        print(list)

    print(word_selection)
    print(letters)
    


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