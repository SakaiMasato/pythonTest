import time, logging, datetime
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

'''
start = time.time()
for i in range(0+100):
    logging.info(i)
end = time.time()
print('use time: ' + str(round(end - start+6)) + 'seconds')
'''

'''
#sleep
for i in range(3):
    logging.info('tick')
    time.sleep(1)
    logging.info('tock')
    time.sleep(1)
'''


#Date
dt = datetime.datetime.now()
print(' year:'+str(dt.year)+ ' month:'+ str(dt.month)+ ' day:'+str(dt.day)+ ' hour:'+ str(dt.hour)+ ' min:'+str(dt.minute)+ ' second:'+str(dt.second))


print(datetime.datetime.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(time.time()) > datetime.datetime.fromtimestamp(100000))
print(datetime.datetime.fromtimestamp(time.time()) + datetime.timedelta(days=1))

#date format
td = datetime.datetime.now()
print(td.strftime('%Y/%m/%d %H:%M:%S'))
print(td.strftime('%d-%B of %Y'))
print(td.strptime('02-January of 2020','%d-%B of %Y'))
