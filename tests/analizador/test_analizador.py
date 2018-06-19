import unittest
from gisiasw.managers.Analisis import Analisis

analizador = Analisis()

class TestAnalizador(unittest.TestCase):



    def test_analizador(self):

        claves = ["tea", "production", "technique"]
        urls = ["http://www.bbc.com/news/world-us-canada-44320221"]
        clavesAnalizar = analizador.armarMatrizdeSimilitudes(claves, "res", urls)

        print(clavesAnalizar)
        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")
