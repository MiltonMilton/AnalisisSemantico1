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
                #Procesa el documento y obtiene el texto. Arreglo de oraciones
                processedDocuments.append(self.procesarDocumento(url))
                #Aplicamos topicModeling para obtener los temas relevantes
                #Aplicamos similaridad Semantica de las clave en el documento
                #Aplicamos otros algoritmos si encontramos
                #ponderamos resultdos. reemplazando en el topicmodeling la similaridad de la clave.

        

        return processedDocuments

    #def otrometodo(self):
        #"topics": topicModeling.analizar(text),

    def procesarDocumento(self, document):
        text = scrapper.buscarHTML("",str(document.get("url")))

        return text