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
import random
from gensim import corpora
import gensim
from gisiasw.scrapper.Scrapper import Scrapper
import time
from datetime import  datetime
import asyncore
import spacyImpl.test


scrapper = Scrapper()
topicModeling = TopicModeling()

class AnalisisSemanticoManager():

    def analizar(self, documents):
        #Recibe la request
        processedDocuments = []

        for document in documents.get("documentos"):
            for url in document.get("urls"):
                processedDocuments.append(self.procesarDocumento(url))
        #Obtiene por cada url una cadena de strings
        #Analiza el contenido
        #Ejecuta el algoritmo de analisis semantico
        #prepara la salida
        #retorna una entidad

        return processedDocuments

    def procesarDocumento(self, document):
        text = scrapper.buscarHTML("",str(document.get("url")))

        return {
            "document": document.get("url"),
            "topics": topicModeling.analizar(text)
        }