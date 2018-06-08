from nltk.corpus import wordnet as wn
import sets

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
    try:
        w1 = wn.synsets(w1)[0]
        w2 = wn.synsets(w2)[0]
        return  w1.wup_similarity(w2)
    except Exception as e:
        return float(0)
        print("no se puede calcular similaridad, se retorna 0,0")
    
