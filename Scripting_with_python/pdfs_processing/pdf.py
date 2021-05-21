import PyPDF2

# with open('dummy.pdf', 'rb') as file: #rb is for reading binary
#     print(file)
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)
    # print(reader.getPage(0)) # the first page
#
#     to tilt a pdf
# page=reader.getPage(0)
# page.rotateCounterClockwise(90)
# writer=PyPDF2.PdfFileWriter()
# writer.addPage(page)
# with open('tilt.pdf', 'wb') as new_file: #wb write binary
#     writer.write(new_file)

# combining pdfs
'''
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    # print(merger)
    for pdf in pdf_list:
        # print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_combiner(inputs)
'''

# watermarking -- a name boldly written in a pdf across the page
template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
# print(template)
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
# print(watermark)
output = PyPDF2.PdfFileWriter()
# print(output)

for i in range(template.getNumPages()):
    # print(i)
    page=template.getPage(i)
    # print(page)
    page.mergePage(watermark.getPage(0)) # cos it has only one page
    output.addPage(page)
#
    with open('watermarked_output.pdf', 'wb') as file: #wb- write binary
        output.write(file)