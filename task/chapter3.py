eggs = 'eggs'
def session1():
    global eggs
    eggs = 'spam'

if __name__ == '__main__':
    session1()
    print(eggs)