from nltk.corpus import wordnet as wn
import sets
import wordninja

def getSinonimo(word):
    sinonimos = []
    for i, j in enumerate(wn.synsets(word)):
        for l in j.lemmas():
            sinonimos.append({
                "word": l.name(),
                "synset": l.synset().name(),
                # "hypernimos": getHipernimo(j.hypernyms()),
                # "hiponimos": [l.lemma_names() for l in j.hyponyms()],
                "tipo": l.synset().lexname().split('.')[0],
                "distance": compareWords(word, l.name()),
                "definition": l.synset().definition(),
                "examples": l.synset().examples()
            })

    return sinonimos

def getListaSinonimos(word):
    lista = []
    syns = wn.synsets(word)
    for ss in range(len(syns)):
        for l in range(len(syns[ss].lemmas())):
            lista.append(syns[ss].lemmas()[l].name())
    return list(sets.Set(lista))

def getHipernimo(hypernimos):
    return [l.lemma_names()for l in hypernimos],

def compareWords(w1, w2):
    w1 = wn.synsets(w1)[0]
    w2 = wn.synsets(w2)[0]
    return  w1.wup_similarity(w2)

def compareWordsSinonimos(w1, w2):
    #igual a compareWords pero si una palabra no tiene synsets
    #busca el primer synset del primer sinonimo, si el primer 
    #sinonimo no tiene synsets, prueba con el segundo sinonimo
    #y asi sucesivamente
    try:
        w1ss = synsetSinonimo(w1)[0]
        w2ss = synsetSinonimo(w2)[0]
        return  w1ss.wup_similarity(w2ss) 
    except Exception as e:
        #no es posible encontrar similiridad para esta palabra
        return float(0)    

def synsetSinonimo(word):#tiene sentido esta funcion? si no tiene synsets tampoco tiene sinonimo
    wss = wn.synsets(word)
    if(len(wss) == 0): #lista vacia?
        print getListaSinonimos(word)
        for sinonimo in getListaSinonimos(word):
            wss = wn.synsets(sinonimo)
            if  (len(wss) != 0): break #encontro un synset
        if(len(wss) == 0): #lista aun vacia?
        #dividimos la palabra:
        #por ejemplo plain_text no tiene sinonimo, pero plain o text si    
            for subword in wordninja.split(word):
                wss = wn.synsets(subword)
                if  (len(wss) != 0): break #encontro un synset
    return wss