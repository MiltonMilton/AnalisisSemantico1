from similaridad import similaridad
from nltk.corpus import wordnet as wn
from gisiasw.algoritmos.Synonim import getListaSinonimos
import random
import re

nouns = []

"""
#usando wornet
limit = 3000
for synset in list(wn.all_synsets("n"))[:limit]:
    for lemma in synset.lemmas():
        nouns.append(lemma.name())
"""

#usando los 1500 most common english nouns

file = open("palabras.txt","r")
for line in file:
    text = re.sub('[\t|\n| ]','',line)
    nouns.append(text)


pruebas = []

c = 0

while (c < 2000):
    noun = random.choice(nouns)
    sinonimos = getListaSinonimos(noun)
    if(len(sinonimos)>0):
        rNoun = random.choice(sinonimos) 
        wup = similaridad(noun,rNoun,"wup")
        sde = similaridad(noun,rNoun,"sde")
        lin = similaridad(noun,rNoun,"lin")
        path = similaridad(noun,rNoun,"path")
        pruebas.append({"w1":noun, "w2":rNoun,"wup":wup,"sde":sde,"lin":lin,"path":path})
    c += 1 

print "{" + "pruebas:["
for prueba in pruebas:
    if prueba.get("wup") != None:
         if prueba.get("sde") != None:
             if prueba.get("lin") != None:
                 if prueba.get("path") != None:
                    print str(prueba) + ","
print "]}"

