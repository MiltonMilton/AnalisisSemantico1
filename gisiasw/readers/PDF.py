import PyPDF2

class PDF:

    def read(self, file):

        content = ''
        pdf = open(file, 'rb')
        reader = PyPDF2.PdfFileReader(pdf)
        for pageNum in range(1, reader.numPages):
            page = reader.getPage(pageNum)
            content += '\n'
            content += page.extractText()

        return content