import pyPDF2
with open('./dummy.pdf', 'rb') as file: #rb is for reading binary
    print(file)
    reader = pyPDF2.pdfFileReader(file)
    print(reader.getpage(0))