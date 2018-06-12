from docx import Document
import os

class Documento:

    def read(self, file):
        print(os.path.abspath(file))
        doc = Document(os.path.abspath(file))
        fullText = []

        for paragraph in doc.paragraphs:
            fullText.append(paragraph.text)

        return '\n'.join(fullText)