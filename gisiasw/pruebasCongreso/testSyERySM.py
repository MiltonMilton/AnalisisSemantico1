from searcher import Searcher
from entityRecognizer import EntityRecognizer
from similarityMeasurer import SimilarityMeasurer

s = Searcher()
er = EntityRecognizer()
sm = SimilarityMeasurer()

def get_values(key):
    #keys = ["machine","learning","python", "algorithms"]

    n = 20
    print("<<<<<<<INITIALIZING GOOGLE>>>>>>>")
    rg = s.search(key.get("it"),"google",n) #resultados google
    print("<<<<<<<INITIALIZING BING>>>>>>>")
    rb = s.search(key.get("it"),"bing",n) #resultados bing
    keys = key.get("keys")
    google = []
    for r in rg:
        g = {}
        g["url"] = str(r)
        entities = er.recognizeAndCheckSynset(r)
        g["entities"] = entities
        meassures = []
        for e in entities:
            for k in keys:
                meassures.append({
                    "value":sm.measure(k,e),
                    "e": e,
                    "k": k
                })
        g["meassures"] = meassures
        google.append(g)
        print g
    bing = []
    for r in rb:
        b = {}
        b["url"] = str(r)
        entities = er.recognizeAndCheckSynset(r)
        b["entities"] = entities
        meassures = []
        for e in entities:
            for k in keys:
                meassures.append({
                    "value":sm.measure(k,e),
                    "e": e,
                    "k": k
                })
        b["meassures"] = meassures
        bing.append(b)
        print(b)

    return {
        "google": google,
        "bing": bing
    }





