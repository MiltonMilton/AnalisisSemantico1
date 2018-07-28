from searcher import Searcher
from entityRecognizer import EntityRecognizer
from similarityMeasurer import SimilarityMeasurer

s = Searcher()
er = EntityRecognizer()
sm = SimilarityMeasurer()



keys = ["machine","learning"]
n = 20

rg = s.search(keys,"google",n) #resultados google
rb = s.search(keys,"bing",n) #resultados bing

print "claves: " + str(keys)
print "numero de resultados por buscador = " + str(n)
print "medidas = wup, sde, lin, path #similarities"


print "----------google-----------"
for r in rg:
    print "url: " + str(r)
    entities = er.recognizeAndCheckSynset(r)
    print "entities: " + str(entities)
    for clave in keys:
        for entity in entities:
            print "clave: " + clave + " ;entidad: " + entity + " ;medidas: " + str(sm.measure(clave,entity))

print "----------bing-----------"
for r in rb:
    print "url: " + str(r)
    entities = er.recognizeAndCheckSynset(r)
    print "entities: " + str(entities)
    for clave in keys:
        for entity in entities:
            print "clave: " + clave + " ;entidad: " + entity + " ;medidas: " + str(sm.measure(clave,entity))