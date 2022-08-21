def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors
    #divisors = [i for i in range(1, num + 1) if num % i == 0]
    divisors = [list(filter(lambda i: num % i == 0, (i for i in range(1, num + 1))))]
    print(divisors)
    print("The program is finished")
    


def run():
    num = int(input('Enter the number: '))
    # divisors = []
    # for i in range(1, num + 1):
    #     divisors.append(i)
    try:
        if num > 0:
            divisors(num)
        else:
            raise ValueError
    except ValueError:
        print('Enter a positive integer number')
            
    




if __name__ == '__main__':
    run()