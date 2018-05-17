import nltk
import spacy
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
class AnalisisSemanticoManager:

    def analizar(self, text):
        #Recibe la request
        #Obtiene por cada url una cadena de strings
        #Analiza el contenido
        #Ejecuta el algoritmo de analisis semantico
        #prepara la salida
        #retorna una entidad
        text_data = []
        for line in text:
            tokens = self.prepare_text_for_lda(line)
            if(random.random() > .99):
                text_data.append(tokens)

        dictionary = corpora.Dictionary(text_data)
        corpus = [dictionary.doc2bow(text) for text in text_data]

        NUM_TOPICS = 5
        ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary, passes=15)
        ldamodel.save('model5.gensim')

        topics = ldamodel.print_topics(num_topics=4)
        return topics

    def tokenize(self, text):
        lda_tokens = []
        tokens = parser(text)
        for token in tokens:
            if(token.orth_.isspace()):
                continue
            elif token.like_url:
                lda_tokens.append('URL')
            #elif token.orth_.start('@'):
            #    lda_tokens.append('SCREEN_NAME')
            else:
                lda_tokens.append(token.lower_)

        return lda_tokens

    def get_lemma(self, word):
        lemma = wn.morphy(word)

        return word if lemma is None else lemma

    def get_lemma2(self, word):
        return WordNetLemmatizer().lemmatize(word)


    def prepare_text_for_lda(self, text):
        tokens = self.tokenize(text)
        tokens = [token for token in tokens if len(token) > 4]
        tokens = [token for token in tokens if token not in en_stop]
        tokens = [self.get_lemma(token) for token in tokens]

        return tokens