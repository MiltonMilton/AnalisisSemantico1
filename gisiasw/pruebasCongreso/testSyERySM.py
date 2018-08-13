from searcher import Searcher
from entityRecognizer import EntityRecognizer
from similarityMeasurer import SimilarityMeasurer
from gisiasw.conceptSimilarity.graph_builder import graph_builder
from gisiasw.conceptSimilarity.Graph import find_path, find_all_paths

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

    n = 20
    print("<<<<<<<INITIALIZING GOOGLE>>>>>>>")
    rg = s.search(key.get("it"),"google",n) #resultados google
    print("<<<<<<<INITIALIZING BING>>>>>>>")
    rb = []#s.search(key.get("it"),"bing",n) #resultados bing
    keys = key.get("keys")
    google = []
    m = {}
    for k in keys:
        m.update({k: graph_builder(nombre=k, nivel=3)})

    for r in rg:
        g = {}
        g["url"] = str(r)
        entities = er.recognizeSinFiltrar(r)
        g["entities"] = [ {"name": x["entidad"], "relevance": x["relevance"], "wiki":x["wiki"]} for x in entities]
        meassures = []
        for j, e in enumerate(entities):
            grafo = graph_builder(nombre=e["entidad"], nivel=3)
            for k in keys:
                ratio = get_ratio(m[k], grafo)
                meassures.append({
                    "relevance": e["relevance"],
                    "e": e["entidad"],
                    "k": k,
                    "ratio": ratio
                })
        g["meassures"] = meassures
        google.append(g)
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
                meassures.append({
                    "value":sm.measure(k,e.get("entidad")),
                    "relevance": e.get("relevance"),
                    "e": e.get("long_name"),
                    "k": k,
                })
        b["meassures"] = meassures
        bing.append(b)

    return {
        "google": google,
        "bing": bing
    }

def get_ratio(key, grafo):
    arreglo_entidad = get_nodes(grafo)
    arreglo_keys = get_nodes(key)
    aes = []
    for i, ae in enumerate(grafo):
        for j, ak in enumerate(key):
            if(ae == ak):
                aes.append(ae)

    denominador = len(arreglo_entidad) + len(arreglo_keys)
    numerador = len(aes)
    ratio = float(numerador) / (float(denominador) - float(numerador))
    print(aes)
    print("ratio: {0} / {1} = {2}".format(numerador, denominador, ratio))
    return ratio

def get_nodes(dic):
    res = []
    for key in dic.keys():
        res.append(key)

    return res




