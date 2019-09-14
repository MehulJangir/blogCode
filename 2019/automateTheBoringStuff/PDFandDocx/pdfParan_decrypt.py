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

			if pdfReader.isEncrypted == True:
				if pdfReader.decrypt(password) == 1:
					pdfWriter = pypdf2.PdfFileWriter()
					for pageNum in range(pdfReader.numPages):
						pdfWriter.addPage(pdfReader.getPage(pageNum))
					if filename.endswith('encrypted.pdf'):
						resultPdf = open(root + '/' + filename[:-13] + 'decrypted.pdf', 'wb')
					else:
						resultPdf = open(root + '/' + filename[:-4] + 'decrypted.pdf', 'wb')
					pdfWriter.write(resultPdf)
					os.remove(root + '/' + filename)
					resultPdf.close()
					pdfFile.close()
				else:
					print('password incorrect for {}'.format(root + '/' + filename))