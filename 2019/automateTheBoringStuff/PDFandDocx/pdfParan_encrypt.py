#! python3

import PyPDF2 as pypdf2
import os

path = str(input('enter root path| '))
password = str(input('enter password| '))

for (root, dirs, files) in os.walk(path):
	for filename in files:
		if filename.endswith('.pdf'):

			pdfFile = open(root + '/' + filename, 'rb')
			pdfReader = pypdf2.PdfFileReader(pdfFile)

			if pdfReader.isEncrypted == False:
				pdfWriter = pypdf2.PdfFileWriter()

				for pageNum in range(pdfReader.numPages):
					pdfWriter.addPage(pdfReader.getPage(pageNum))

				pdfWriter.encrypt(password)

				if filename.endswith('decrypted.pdf'):
					resultPdf = open(root + '/' + filename[:-13] + 'encrypted.pdf', 'wb')
				else:
					resultPdf = open(root + '/' + filename[:-4] + 'encrypted.pdf', 'wb')

				pdfWriter.write(resultPdf)
				pdfWriter.write(resultPdf)
				os.remove(root + '/' + filename)
				resultPdf.close()
				pdfFile.close()