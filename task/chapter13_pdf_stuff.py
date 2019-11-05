import PyPDF2, logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s- %(message)s')

pdfFileObj = open('Regular-Expression-Tutorial.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# pdfReader.isEncrypted    (check is encrypted or not)
# pdfReader.decrypt('password')    (pass pwd to reader)
# pdfWriter.encrypt('password')    (encrypt pdf)
logging.info('numPages: ' + str(pdfReader.numPages))
pageObj = pdfReader.getPage(0)
#pageObj.rotateClockwise(90)  ## rotate page
#pageObj.mergePage(pdfWaterMarkReader.getPage(0))  ## add water  mark
logging.info(pageObj.extractText())

#######################copy pdf################################
'''
######can not modify pdf directly
pdfFile1 = open('Regular-Expression-Tutorial.pdf', 'rb')
pdfReader1 = PyPDF2.PdfFileReader(pdfFile1)
pdfWriter = PyPDF2.PdfFileWriter()
#pdfWriter.encrypt('password')      #encrypt pdf
for pageNum in range(pdfReader1.numPages):
    pageObj = pdfReader1.getPage(pageNum)
    pdfWriter.addPage(pageObj)
pdfOutFile = open('Regular-Expression-Tutorial2.pdf', 'wb')
pdfWriter.write(pdfOutFile)
pdfOutFile.close()
pdfFile1.close()
'''


