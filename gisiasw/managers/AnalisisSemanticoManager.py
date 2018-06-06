import nltk
import spacy

from gisiasw.algoritmos.TopicModeling import TopicModeling

nltk.download('wordnet')
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer
spacy.load('en')
from spacy.lang.en import English
parser = English()
nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
from gisiasw.scrapper.Scrapper import Scrapper
from gisiasw.algoritmos.Synonim import getSinonimo, getListaSinonimos
from gisiasw.formatter.formatter import format

scrapper = Scrapper()
topicModeling = TopicModeling()

class AnalisisSemanticoManager():

    def analizar(self, documents):
        #Recibe la request
        processedDocuments = []

        for document in documents.get("documentos"):
            for clave in documents.get('claves'):
                processedDocuments.append({
                        "word": clave,
                        "ponderacion": 0,
                        "sinonimos": getSinonimo(clave),
                        "tipo": "CLAVE"
                    })

            for url in document.get("urls"):
                #Procesa el documento y obtiene el texto. Arreglo de oraciones
                #Aplicamos topicModeling para obtener los temas relevantes
                topicos = self.procesarDocumento(url)
                print(topicos)
                for i in range(len(topicos)):
                    print(topicos[i])
                    topico = topicos[i]
                    processedDocuments.append({
                        "word": topico.get('word'),
                        "ponderacion":topico.get('ponderacion'),
                        "sinonimos": getListaSinonimos(topico.get('word')),
                        "tipo": "TOPIC"
                    })
                #Aplicamos similaridad Semantica de las clave en el documento
                #Aplicamos otros algoritmos si encontramos
                #ponderamos resultdos. reemplazando en el topicmodeling la similaridad de la clave.

        

        return format(processedDocuments)

    #def otrometodo(self):
        #"topics": topicModeling.analizar(text),

    def procesarDocumento(self, document):
        text = scrapper.buscarHTML("",str(document.get("url")))

        return topicModeling.analizar(text)

    def procesarURL(self, url):
        text = scrapper.buscarHTML("",url)

        return topicModeling.analizar(text)

    