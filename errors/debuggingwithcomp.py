def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = int(input('Enter the number: '))
    print(divisors(num))
    print("The program is finished")


if __name__ == '__main__':
    run()