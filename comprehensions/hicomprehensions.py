def run():

    # print square numbers from 1-100 that are just divisible by 3
    #list = []
    #for i in range(1,101):
        #if i%3 !=0:
            #list.append(i**2)
    #print(list)

    list = [i for i in range(1,101) if i %3 != 0]
    print(list)


if __name__ == '__main__':
    run()
