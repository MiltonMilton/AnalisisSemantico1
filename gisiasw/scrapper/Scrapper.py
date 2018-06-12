from bs4 import BeautifulSoup
from bs4 import Comment
import requests as rq
import urllib
import time
from gisiasw.readers.PDF import PDF
from gisiasw.readers.Documento import Documento
# from pattern.web import plaintext

class Scrapper:

    def buscarHTML(self, nombre, url):
        try:
            page = rq.get(url)
            soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
            #extrae tags sin contenido relevante para analisis
            [x.extract() for x in soup.find_all('script')]
            [x.extract() for x in soup.find_all('style')]
            [x.extract() for x in soup.find_all('meta')]
            [x.extract() for x in soup.find_all('noscript')]

            [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

            cleanText = [x for x in soup.get_text().split('\n') if (x != "") and (x!=" ")]

            #print("cleanText", cleanText)
            #return plaintext(soup.get_text())
            return cleanText

        except Exception as e:
            print "Error Retrieving data: ", url, ": ", str(e)
            pass

    def buscarHtmlCompleto(self, url):
        page = rq.get(url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
        # extrae tags sin contenido relevante para analisis
        [x.extract() for x in soup.find_all('script')]
        [x.extract() for x in soup.find_all('style')]
        [x.extract() for x in soup.find_all('meta')]
        [x.extract() for x in soup.find_all('noscript')]

        [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

        return soup.get_text()

    def buscarPDF(self, nombre, url):
        fileData = urllib.urlopen(url)
        datatowrite = fileData.read()
        tmpFileName ='/tmp/'+str(time.time())+'.pdf'

        with open(tmpFileName, 'wb') as f:
            f.write(datatowrite)

        pdf = PDF()
        return pdf.read(tmpFileName)

    def buscarDoc(self, nombre, url):
        tmpFileName = str(time.time())
        fileData = urllib.urlretrieve(url, tmpFileName)

        documento = Documento()

        return documento.read(tmpFileName)