from searcher import Searcher
from entityRecognizer import EntityRecognizer
from gisiasw.scrapper.Scrapper import Scrapper
import spotlight

s = Searcher()
er = EntityRecognizer()
scrap =Scrapper()

keys = ["machine","learning","python"]
n = 10

rg = s.search(keys,"google",n) #resultados google
rb = s.search(keys,"bing",n) #resultados bing



for r in rg:
    print "<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    print "url: " + str(r)
    text = scrap.buscarHTML("",str(r))
    annotations = spotlight.annotate('http://api.dbpedia-spotlight.org/en/annotate',
                                     text=text,
                                     confidence=0.4, support=10)

    for k,an in enumerate(annotations):
        print(an)
        print("surfaceForm: {0}".format(an.get("surfaceForm")))
        print("Type: {0}".format(an.get("types")))
        print "-------------------------------------------"


