from searcher import Searcher
from entityRecognizer import EntityRecognizer
from similarityMeasurer import SimilarityMeasurer

s = Searcher()
er = EntityRecognizer()
sm = SimilarityMeasurer()

keys = ["machine","learning","python"]
n = 10

rg = s.search(keys,"google",n) #resultados google
rb = s.search(keys,"bing",n) #resultados bing

for r in rg:
    for e in er.recognize(r):
        for k in keys:
            print sm.measure(k,e)

