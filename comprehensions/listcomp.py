def run():
    list = [] 
    list = [ i for i in range(0,100000) if i %9 == 0 and i %6 == 0 and i %4 == 0]
    print(list)


if __name__ == '__main__':
    run()
