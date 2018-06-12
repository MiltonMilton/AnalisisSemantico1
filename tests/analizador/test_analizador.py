import unittest
from gisiasw.managers.Analisis import Analisis

analizador = Analisis()

class TestAnalizador(unittest.TestCase):



    def test_analizador(self):

        claves = ["tea", "production", "technique"]
        clavesAnalizar = analizador.armarMatrizdeSimilitudes(claves)

        print(clavesAnalizar)
        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")
