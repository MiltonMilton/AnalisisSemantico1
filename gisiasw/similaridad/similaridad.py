from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import nltk
nltk.download('brown')
nltk.download('wordnet_ic')


def similaridad(word1, word2, metodo):

    switch = {
        "jcn": jcnSimilarity,
        "lch": lchSimilarity,
        "lin": linSimilarity,
        "path": pathSimilarity,
        "res": resSimilarity,
        "wup": wupSimilarity,
        "byWeight": byWeight
    }

    res = 0
    try:

        w1 = wn.synsets(word1)[0]
        w2 = wn.synsets(word2)[0]

        func = switch.get(metodo)
        res = func(w1, w2)
    except Exception as e:
        print(word1, word2, e.message)
        print("Error calculando similitud, se pondera 0")

    return res

def jcnSimilarity(word1, word2):
    ##Needs the corpus
    brown_ic = wordnet_ic.ic('ic-brown.dat')

    return word1.jcn_similarity(word2, brown_ic)

def lchSimilarity(word1, word2):
    return word1.lch_similarity(word2)


def linSimilarity(word1, word2):
    ##Needs the corpus
    brown_ic = wordnet_ic.ic('ic-brown.dat')
    semcor_ic = wordnet_ic.ic('ic-semcor.dat')
    return word1.lin_similarity(word2,brown_ic)

def pathSimilarity(word1, word2):

    return word1.path_similarity(word2)

def resSimilarity(word1, word2):
    brown_ic = wordnet_ic.ic('ic-brown.dat')

    return word1.res_similarity(word2, brown_ic)

def wupSimilarity(word1, word2):

    return word1.wup_similarity(word2)

def byWeight():
    return 0