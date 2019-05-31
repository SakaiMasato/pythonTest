def task9(spam):
    if (spam == 1):
        print('Hello')
    elif (spam == 2):
        print('Howdy')
    else:
        print('Greetings')

def task13():
    for i in range(10):
        print(i, end = '')

    print('\nhello', 'world', sep = ',')
    n = 0
    while n < 10:
        print(n, end = '')
        n += 1

if __name__ == '__main__':
    #task9(1)
    task13()