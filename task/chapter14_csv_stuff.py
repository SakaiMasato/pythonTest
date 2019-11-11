import csv, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

example = open('csvTest.csv')
exampleReader = csv.reader(example)
#loop datas
for row in exampleReader:
    logging.info(str(exampleReader.line_num) + ' ' + str(row))
example.close()

example = open('csvTest.csv')
exampleReader = csv.reader(example)
exampleData = list(exampleReader)
logging.info(exampleData)
logging.info(exampleData[0][0])
example.close()

#append something
example = open('csvTest.csv', 'a', newline='')
writer = csv.writer(example)
#csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')     using tab as a seperator, applying two lines as a interval
writer.writerow(['4/10/2015 5:25','watermelon','100'])
example.close()

