from pyfiglet import Figlet
import random
import os 


def game(words, new_width=100):
    
    # word selection
    word_selection = random.choice(words)
    #word_selection = "holaamigo"
    # create a lit comp for letter in word
    letters = [letter for letter in word_selection if letter != '\n']
    time_try = 7


    list = letters[:]
    # replace letters with '_'
    for i, n in enumerate(list):
        list[i] = "_"

    #figlet title ASCII
    fuente = Figlet(font='rozzo')
    print(fuente.renderText(' HANGMAN  GAME ')) 
    print(f'You have {time_try} tries left')
    print(''' 
                    ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y . .  ||
                    | |       // |   | ||
                    | |      //  | . | ||
                    | |     ')   |   | (`
                    | |          ||'||
                    | |          || ||
                    | |          || ||
                    | |          || ||
                    | |          || ||
                    """"""""""|_`-' `-' |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  

    print(f' \n {list}')
    
    
                
    for i in range(7):      

    # ask the user to input a letter they want to guess from word
        single_letter = input(str('\n Please enter the letter to check: \n\n '))
        time_try -= 1 

        



    #compare single letter with all letters to match
        for index_val, elem in enumerate(letters):

            if single_letter == elem:
                os.system('clear')

                fuente = Figlet(font='rozzo')
                print(fuente.renderText('\n HANGMAN  GAME'))

                print(f'You have {time_try} tries left')
                list[index_val] = elem
                
                # working on this
                # list_entry = [i+i for i in single_letter ]
                # print(list_entry)
                
                if list != letters:
                    print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      
                    | |/ /       
                    | | /       
                    | |/        
                    | |         
                    | |         
                    | |       keep guessing you might win  
                    | |              
                    | |     
                    | |                 :)
                    | | 
                    | |         
                    | |         
                    | |         
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')
                else:
                    print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      
                    | |/ /       
                    | | /       
                    | |/        
                    | |         ¡ TIME TO CELEBRATE ! 
                    | |         
                    | |          
                    | |     (read down to discover the word)
                    | |      
                    | |                  :)
                    | |          
                    | |              play again
                    | | 
                    | |        
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')


        if single_letter not in letters:
            #print('\n UPSSSS try again  \n')   
            os.system('clear')

            fuente = Figlet(font='rozzo')
            print(fuente.renderText('\n HANGMAN  GAME'))

            print(f'You have {time_try} tries left, Try again... ')

            
            if time_try == 7:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      
                    | |/ /       
                    | | /       
                    | |/        
                    | |         
                    | |         
                    | |        
                    | |       
                    | |      
                    | |    
                    | |          
                    | |         
                    | |         
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  
            elif time_try == 6:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||
                    | |/         ||
                    | |          ||  
                    | |          (\_
                    | |           `--'
                    | |       
                    | |      
                    | |  
                    | |     
                    | |          
                    | |          
                    | |          
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  
            elif time_try == 5:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |        
                    | |       
                    | |     
                    | |      
                    | |     
                    | |          
                    | |          
                    | |          
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  
            elif time_try == 4:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y 
                    | |       // 
                    | |      //  
                    | |     ')  
                    | |          
                    | |          
                    | |          
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''') 
            elif time_try == 3:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y . .  
                    | |       // |   | 
                    | |      //  | . | 
                    | |     ')   |   | 
                    | |          
                    | |          
                    | |          
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')    
            elif time_try == 2:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y . .  ||
                    | |       // |   | ||
                    | |      //  | . | ||
                    | |     ')   |   | (`
                    | |          
                    | |         
                    | |          
                    | |          
                    | |        
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  
            elif time_try == 1:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y . .  ||
                    | |       // |   | ||
                    | |      //  | . | ||
                    | |     ')   |   | (`
                    | |          ||'
                    | |          || 
                    | |          || 
                    | |          || 
                    | |          || 
                    """"""""""|_`-'     |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')  
            elif time_try == 0:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      ||
                    | |/ /       ||
                    | | /        ||.-"".
                    | |/         ||/  _ |
                    | |          ||  `/,|
                    | |          (\_ `_.'
                    | |         .-`--'.
                    | |        /Y . .  ||
                    | |       // |   | ||
                    | |      //  | . | ||
                    | |     ')   |   | (`
                    | |          ||'||
                    | |          || ||
                    | | ¡YOU ARE || || DEAD!
                    | |          || ||
                    | |          || ||
                    """"""""""|_`-' `-' |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''') 
            else:
                print(''' 
                     ___________.._______
                    | .__________))______|
                    | | / /      
                    | |/ /       
                    | | /       
                    | |/        
                    | |         
                    | |         
                    | |        
                    | |       
                    | |      
                    | |    
                    | |          
                    | |         
                    | |         
                    | |          
                    | |          
                    """"""""""|_        |"""|
                    |"|"""""""\ \       '"|"|
                    | |        \ \        | | 
                    : :         \ \       : :  
                    . .          `'       . . sk ''')


        print(f' \n {list}')

    if list != letters:
        print(f'\n You lost ! The word is: {word_selection} \n ')
    else:
        print(f'\n You a winner ! The word is: {word_selection} \n ')      
            


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