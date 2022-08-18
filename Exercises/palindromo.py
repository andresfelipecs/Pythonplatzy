def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('write a word: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        palabra = palabra.replace(' ', '')
        palabra = palabra.lower()
        print( str(palabra) + ' : is palíndromo')
    else:
        print('it is not palíndromo')


if __name__ == '__main__':
    run()