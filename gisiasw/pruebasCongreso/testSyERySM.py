from searcher import Searcher
from entityRecognizer import EntityRecognizer
from similarityMeasurer import SimilarityMeasurer

s = Searcher()
er = EntityRecognizer()
sm = SimilarityMeasurer()
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
lemmatizer = WordNetLemmatizer()


def get_values(key):
    #keys = ["machine","learning","python", "algorithms"]

    n = 1
    print("<<<<<<<INITIALIZING GOOGLE>>>>>>>")
    rg = s.search(key.get("it"),"google",n) #resultados google
    print("<<<<<<<INITIALIZING BING>>>>>>>")
    rb = s.search(key.get("it"),"bing",n) #resultados bing
    keys = key.get("keys")
    google = []
    for r in rg:
        g = {}
        g["url"] = str(r)
        entities = er.recognizeSinFiltrar(r)
        g["entities"] = [ {"name": x["long_name"], "relevance": x["relevance"], "wiki":x["wiki"]} for x in entities]
        meassures = []
        for j, e in enumerate(entities):
            for k in keys:
                print(nltk.pos_tag(nltk.word_tokenize(e["long_name"])))
                meassures.append({
                    "value": sm.measure(k, e["long_name"]),
                    "relevance": e["relevance"],
                    "e": e["long_name"],
                    "k": k
                })
        g["meassures"] = meassures
        google.append(g)
        print g
    bing = []
    for r in rb:
        b = {}
        b["url"] = str(r)
        entities = er.recognizeSinFiltrar(r)
        b["entities"] = [{"name": x["long_name"], "relevance": x["relevance"]} for x in entities]
        meassures = []
        for j, e in enumerate(entities):
            print(e["entidad"])
            for k in keys:
                print(lemmatizer.lemmatize(e.get("long_name")))
                meassures.append({
                    "value":sm.measure(k,e.get("entidad")),
                    "relevance": e.get("relevance"),
                    "e": e.get("long_name"),
                    "k": k
                })
        b["meassures"] = meassures
        bing.append(b)
        print(b)

    return {
        "google": google,
        "bing": bing
    }





