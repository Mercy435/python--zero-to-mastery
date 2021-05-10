import PyPDF2
with open('pdf_folder/11.2 dummy.pdf', 'rb') as file: #rb is for reading binary
    print(file)
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getPage(0))