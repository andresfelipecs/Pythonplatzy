import time

def factorial(n):
    answer = 1

    while n > 1:
        answer *= n
        n -= 1
        

    return answer


def factorial_r(n):
    for i in range(1, n):
        return f"{i * (i+1)} "
    # if n == 1:
    #     return 1

    # return n * factorial_r(n - 1)


if __name__ == '__main__':
    n = 200000

    start = time.time()
    factorial(n)
    end = time.time()
    print(end - start)

    start = time.time()
    factorial_r(n)
    end = time.time()
    print(end - start)