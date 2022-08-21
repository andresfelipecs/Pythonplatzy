#def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors
    #divisors = [i for i in range(1, num + 1) if num % i == 0]
    
    


def run():
    num = int(input('Enter the number: '))
    # divisors = []
    # for i in range(1, num + 1):
    #     divisors.append(i)
    divisors = [list(filter(lambda i: num % i == 0, (i for i in range(1, num + 1))))]
    print(divisors)
    print("The program is finished")


if __name__ == '__main__':
    run()