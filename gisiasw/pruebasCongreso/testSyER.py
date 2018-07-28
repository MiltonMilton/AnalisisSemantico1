from searcher import Searcher
from entityRecognizer import EntityRecognizer

s = Searcher()
er = EntityRecognizer()

keys = ["machine","learning","python"]
n = 10

rg = s.search(keys,"google",n) #resultados google
rb = s.search(keys,"bing",n) #resultados bing


print "----------google-----------"
for r in rg:
    print "url: " + str(r)
    print "entities: " + str(er.recognizeAndCheckSynset(r))

print "----------bing-----------"
for r in rb:
    print "url: " + str(r)
    print "entities: " + str(er.recognizeAndCheckSynset(r))