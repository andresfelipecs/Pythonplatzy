
#imprime la tabla del 3,6,7,8,0

def mul(number,number1):
    LIMIT = 10
    contador = 1
    resultado = number1*contador
    print('You have chosen the table of' + number)
    while(contador < LIMIT):
        print(str(resultado))
        contador += 1
        resultado = number1*contador
    print("🔥Thank you for proving the programm🔥")

menu = """
Welcome to the menu done by Felipe for the multiplication tables of the numbers 3,6,7,8,0. 
Please select which multiplication table do you want:

1- table of 3
2- table of 6
3- table of 7
4- table of 8
5- table of 0
"""
def run():

    opcion = int(input(menu))
    if opcion == 1:
        mul("the number 3", 3)
    elif opcion == 2:
        mul("the number 6", 6)
    elif opcion == 3:
        mul("the number 7", 7)
    elif opcion == 4:
        mul("the number 8", 8)
    elif opcion == 5:
        mul("the number 0", 0)
    else:
        print('please enter a correct option')


if __name__ == '__main__':
    run()
