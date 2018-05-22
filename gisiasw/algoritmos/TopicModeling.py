# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy

# NLTK Stop words
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
nlp = spacy.load('en', disable=['parser', 'ner'])

class TopicModeling:
    bigram = []
    trigram = []
    bigram_mod = []
    trigram_mod = []

    def analizar(self, text):
        try:
            # en el tutorial utiliza str(sentencia) pero tira un unicodeError, por eso lo cambie por encode
            data_words = list(self.sent_to_words(text))

            bigram = gensim.models.Phrases(data_words, min_count=5, threshold=100)  # higher threshold fewer phrases.
            trigram = gensim.models.Phrases(bigram[data_words], threshold=100)

            # Faster way to get a sentence clubbed as a trigram/bigram
            self.bigram_mod = gensim.models.phrases.Phraser(bigram)
            self.trigram_mod = gensim.models.phrases.Phraser(trigram)

            # Remove Stop Words
            data_words_nostops = self.remove_stopwords(data_words)

            # Form Bigrams
            data_words_bigrams = self.make_bigrams(data_words_nostops)

            # Initialize spacyImpl 'en' model, keeping only tagger component (for efficiency)
            # python3 -m spacyImpl download en
            nlp = spacy.load('en', disable=['parser', 'ner'])

            # Do lemmatization keeping only noun, adj, vb, adv
            aux = []
            for i in data_words_bigrams:
                if not (i == []):
                    aux.append(i)
            data_words_bigrams = aux

            print(data_words_bigrams)

            data_lemmatized = self.lemmatization(data_words_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'])

            # print(data_lemmatized[:1])

            # #######################

            # Create Dictionary
            id2word = corpora.Dictionary(data_lemmatized)

            # Create Corpus
            texts = data_lemmatized

            # Term Document Frequency
            corpus = [id2word.doc2bow(text) for text in texts]

            lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                                        id2word=id2word,
                                                        num_topics=3,
                                                        random_state=100,
                                                        update_every=1,
                                                        chunksize=100,
                                                        passes=10,
                                                        alpha='auto',
                                                        per_word_topics=True)

            #pprint(lda_model.print_topics())
            doc_lda = lda_model[corpus]
            #print(doc_lda[1])
            return lda_model.print_topics()
        except Exception as e:
            print "Error en TopicMOdeling: ", text, ": ", str(e)
            pass

    # # Define functions for stopwords, bigrams, trigrams and lemmatization
    def remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    def make_bigrams(self, texts):
        return [self.bigram_mod[doc] for doc in texts]

    def make_trigrams(self, texts):
        return [self.trigram_mod[self.bigram_mod[doc]] for doc in texts]

    def lemmatization(self, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacyImpl.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    def sent_to_words(self, sentences):

        for sentence in sentences:
            print("SENTENCE: ", sentence)
            try:
                yield (gensim.utils.simple_preprocess(sentence.encode('ascii', 'ignore'), deacc=True))  # deacc=True removes punctuations
            finally:
                pass
