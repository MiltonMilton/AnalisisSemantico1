from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
import nltk
nltk.download('brown')
nltk.download('wordnet_ic')
import math


def similaridad(word1, word2, metodo):

    switch = {
        "jcn": jcnSimilarity,
        "lch": lchSimilarity,
        "lin": linSimilarity,
        "path": pathSimilarity,
        "res": resSimilarity,
        "wup": wupSimilarity,
        "byWeight": byWeight,
        "sde": SDE_Similarity,
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
def similitudPorAlgoritmo(word1, word2):
    res = 0
    try:
        w1 = wn.synsets(word1)[0]
        w2 = wn.synsets(word2)[0]
        return  {
            #"jcn": jcnSimilarity(w1,w2),
            #"lch": lchSimilarity(w1,w2),
            "lin": linSimilarity(w1,w2),
            "path": pathSimilarity(w1,w2),
            #"res": resSimilarity(w1,w2),
            "wup": wupSimilarity(w1,w2),
            "SDE": SDE_Similarity(w1,w2)
            #"byWeight": byWeight(w1,w2)
        }
    except Exception as e:
        print(word1, word2, e.message)
        print("Error calculando similitud, se pondera 0")

    return {
        "lin": 0,
        "path": 0,
        "wup": 0,
        "SDE": 0
        # "byWeight": byWeight(w1,w2)
    }

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
    return word1.lin_similarity(word2,brown_ic, verbose=True)

def pathSimilarity(word1, word2):

    return word1.path_similarity(word2)

def resSimilarity(word1, word2):
    brown_ic = wordnet_ic.ic('ic-brown.dat')

    return word1.res_similarity(word2, brown_ic)

def wupSimilarity(word1, word2):

    return word1.wup_similarity(word2)

def byWeight():
    return 0

def SDE_Similarity(word1,word2,alfa=0.2,beta=0.45,verbose=False, simulate_root=True):
    #la del paper de sentence similarity de la universidad de Ulster
    #SDE: Scaling Depth Effect
    #l: shortest path lenght (desde una palabra hasta el antecesor comun)
    #h: depth of subcomer in the heirarchical semantic net
    #math.exp(A) es lo mismo que decir: e "elevado a la" A
    
    need_root = word1._needs_root()

    subsumers = word1.lowest_common_hypernyms(
        word2,
        simulate_root=simulate_root and need_root, use_min_depth=True
    )
    
    if len(subsumers) == 0:
        return None

    subsumer = word1 if word1 in subsumers else subsumers[0]

    depth = subsumer.max_depth() + 1
    
    len1 = word1.shortest_path_distance(
        subsumer,
        simulate_root=simulate_root and need_root
    )
    len2 = word2.shortest_path_distance(
        subsumer,
        simulate_root=simulate_root and need_root
    )
    if len1 is None or len2 is None:
        return None
    #para saber xq comento esto ver:
    #https://arxiv.org/pdf/1211.4709.pdf
    #pag.24
    # len1 += depth
    # len2 += depth
    h = depth
    l = min(len1,len2)
    numerador = (math.exp(-1 * alfa * l )) * ( math.exp(beta * h) - math.exp(-1 * beta * h))
    denominador = (math.exp(beta * h) + math.exp(-1 * beta * h))
    
    # print "len1" + str(len1) + " len2 " + str(len2) + " h " + str(h) + " l " + str(l) + " numerador " + str(numerador) + " denominador " + str(denominador) 

    return (numerador/denominador)


