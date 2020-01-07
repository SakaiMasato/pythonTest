import threading, time

print('Start of program')


def takeANap():
    time.sleep(3)
    print('wake up!')


thread = threading.Thread(target=takeANap)
thread.start()
print('End of Program')


def lazyCal(a, b):
    print(a + b)


nums = [1,2]
thread = threading.Thread(target=lazyCal, args=nums)
thread.start()
