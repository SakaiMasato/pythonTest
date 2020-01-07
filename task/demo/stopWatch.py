import time, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

data = []
index = 0
singletime = 0

print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.Press Ctrl-C to quit.')
input()
print('start')
startTime = round(time.time(), 2)
endTime = startTime
index = 1
try:
    while True:
        if(input() == 'q'):
            print('Done')
            break
        print('lap time: ' + str(index))
        endTime = round(time.time(),2)
        data.append({str(index): endTime - startTime})
        startTime = endTime
        index += 1
        print(data)
except KeyboardInterrupt:
    print('Done')


