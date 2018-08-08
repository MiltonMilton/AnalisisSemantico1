import unittest
from gisiasw.managers.CongresoManager import CongresoManager
congreso = CongresoManager()
from gisiasw.pruebasCongreso.searcher import Searcher
from gisiasw.pruebasCongreso.entityRecognizer import EntityRecognizer
from gisiasw.pruebasCongreso.similarityMeasurer import SimilarityMeasurer

s = Searcher()
er = EntityRecognizer()
from gisiasw.pruebasCongreso.entityRecognizer import EntityRecognizer
er = EntityRecognizer()
sm = SimilarityMeasurer()
GOOGLE = "google"
BING = "bing"
busqueda_1 = "Machine Learning"
busqueda_2 = "Machine Learning python"
busqueda_3 = "Machine Learning python algorithms"

class TestCongreso(unittest.TestCase):



    def test_busqueda_1_google(self):
        l = {"it": ["'machine learning'","python", "algorithms"], "keys": ["machine","learning","python", "algorithms"]}
        keys = l.get("keys")
        #resultados = er.recognizeSinFiltrar("http://essentit.com/ngc/test.html")
        m = ["http://essentit.com/ngc/test.html"]
        for r in m:
            g = {}
            g["url"] = str(r)
            entities, index = er.recognizeSinFiltrar(r)
            g["entities"] = index
            meassures = []
            for j, e in enumerate(entities):
                for k in keys:
                    meassures.append({
                        "value": sm.measure(k, e.get("entidad")),
                        "relevance": sm.measure(k, e.get("relevance")),
                        "e": e.get("long_name"),
                        "k": k
                    })
            g["meassures"] = meassures
            google.append(g)
            print g
        self.assertTrue(True)

    def test_busqueda_2_google(self):

        resultados = congreso.initialize(GOOGLE, busqueda_2)
        print(resultados)
        self.assertTrue(True)

    def test_busqueda_3_google(self):

        resultados = congreso.initialize(GOOGLE, busqueda_3)
        print(resultados)
        self.assertTrue(True)
