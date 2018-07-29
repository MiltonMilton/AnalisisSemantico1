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

            #extrae tags sin contenido relevante para analisis
            #[x.extract() for x in soup.find_all('script')]
            #[x.extract() for x in soup.find_all('style')]
            #[x.extract() for x in soup.find_all('meta')]
            #[x.extract() for x in soup.find_all('noscript')]
            #[x.extract() for x in soup.find_all('p')]
            #[x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

            #cleanText = [x for x in soup.get_text().split('\n') if (x != "") and (x!=" ")]

            #print("cleanText", cleanText)
            #return plaintext(soup.get_text())
            #return soup.find_all('p')
            return self.text_from_html(page.content).encode("utf-8")

        except Exception as e:
            print "Error Retrieving data: ", url, ": ", str(e)
            pass

    def tag_visible(self, element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    def text_from_html(self,body):
        soup = BeautifulSoup(body, 'html.parser', from_encoding="utf-8")
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)

    def buscarHtmlCompleto(self, url):
        page = rq.get(url)
        soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
        # extrae tags sin contenido relevante para analisis
        [x.extract() for x in soup.find_all('script')]
        [x.extract() for x in soup.find_all('style')]
        [x.extract() for x in soup.find_all('meta')]
        [x.extract() for x in soup.find_all('noscript')]

        [x.extract() for x in soup.find_all(text=lambda text: isinstance(text, Comment))]

        return soup.get_text().replace('\n', " ")

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
