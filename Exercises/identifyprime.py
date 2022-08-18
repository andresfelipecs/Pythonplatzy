#Para saber si un número es primo (divisible sólo por el mismo y por uno), lo dividimos sucesivamente por los primeros números primos: 2, 3, 5, 7, 11, ..
#¿Cuándo paramos de dividir?

#- Si obtenemos división exacta \ no es primo
#- Si el cociente es menor que el divisor .. paramos \ es primo

#Ejemplo: 113

#- 113 no es divisible por 2 (divisor: 2 , cociente: 56.5)
#- 113 no es divisible por 3 (divisor: 3 , cociente: 37’ ..)
#- 113 no es divisible por 5 (divisor: 5 , cociente: 22’ ..)
#- 113 no es divisible por 7 (divisor: 7 , cociente: 16’ ..)
#- 113 no es divisible por 11 (divisor: 11 , cociente: 10’ ..)
#Paramos pues el cociente es menor que el divisor \ 113 es primo

#Introduce aquí debajo cualquier número para comprobar si es primo
def condition(number):
    resultado = number % 2
    resultado1 = number % 3
    resultado2 = number % 5
    resultado3 = number % 7
    resultado4 = number % 11 
    cociente = number // 2
    cociente1 = number // 3 
    cociente2 = number // 5
    cociente3 = number // 7
    cociente4 = number // 11
    if number == 2 or number == 3 or number == 5 or number == 7 or number ==11:
        print('The number ' + str(number) + ' is prime')
    elif resultado == 0 or resultado1 == 0 or resultado2 == 0 or resultado3 == 0 or resultado4 == 0:
            print('The number ' + str(number) + ' is not a prime')
    elif cociente < 2 or cociente1 < 3 or cociente2 < 5 or cociente3 < 7 or cociente4 < 11:
        print('The number ' + str(number) + ' is prime')
    else:
        print('enter a proper number')
                                       
def run():
    number = int(input('Please enter the number: '))
    if number == 1 or number <= 0:
        print('The number ' + str(number) + ' is not prime')
    elif number != 1 or number !=0 or number >= 2:
            condition(number)  
    else:
            print('The number ' + str(number) + ' is not prime') 
            
if __name__ == '__main__':
    run()