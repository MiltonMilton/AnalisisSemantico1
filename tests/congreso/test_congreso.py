import unittest
from gisiasw.managers.CongresoManager import CongresoManager
congreso = CongresoManager()

GOOGLE = "google"
BING = "bing"
busqueda_1 = "Machine Learning"
busqueda_2 = "Machine Learning python"
busqueda_3 = "Machine Learning python algorithms"

class TestCongreso(unittest.TestCase):



    def test_busqueda_1_google(self):

        resultados = congreso.initialize(GOOGLE, busqueda_1)
        print(resultados)
        self.assertTrue(True)

    def test_busqueda_2_google(self):

        resultados = congreso.initialize(GOOGLE, busqueda_2)
        print(resultados)
        self.assertTrue(True)

    def test_busqueda_3_google(self):

        resultados = congreso.initialize(GOOGLE, busqueda_3)
        print(resultados)
        self.assertTrue(True)
