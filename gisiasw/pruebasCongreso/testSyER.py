from searcher import Searcher
from entityRecognizer import EntityRecognizer

s = Searcher()
er = EntityRecognizer()

keys = ["machine","learning","python"]
n = 10

rg = s.search(keys,"google",n) #resultados google
rb = s.search(keys,"bing",n) #resultados bing

print er.recognize(rg[0])