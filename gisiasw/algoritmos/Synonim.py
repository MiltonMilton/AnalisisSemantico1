from nltk.corpus import wordnet as wn

def getSinonimo(word):
    sinonimos = []
    for i, j in enumerate(wn.synsets(word)):
        for l in j.lemmas():
            sinonimos.append({
                "word": l.name(),
                "synset": l.synset().name(),
                #"hypernimos": getHipernimo(j.hypernyms()),
                #"hiponimos": [l.lemma_names() for l in j.hyponyms()],
                "tipo": l.synset().lexname().split('.')[0],
                "distance": compareWords(word, l.name()),
                "definition": l.synset().definition(),
                "examples": l.synset().examples()
            })

    return sinonimos

def getHipernimo(hypernimos):
    return [l.lemma_names()for l in hypernimos],

def compareWords(w1, w2):
    w1 = wn.synsets(w1)[0]
    w2 = wn.synsets(w2)[0]
    return  w1.wup_similarity(w2)