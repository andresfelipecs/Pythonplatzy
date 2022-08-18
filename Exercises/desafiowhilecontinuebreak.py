from re import I


def run():
    i = int(input('Please enter the start number: '))
    print(i)
    while i < 500:
        if i > 100:
            continue
        print(i+1)
        i += 1


if __name__ == '__main__':
    run()