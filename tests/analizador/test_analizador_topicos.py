import unittest
from gisiasw.analizadores.AnalizadorTopicos import AnalizadorTopicos

analizador = AnalizadorTopicos()
class TestAnalizadorTopicos(unittest.TestCase):


    def test_analizador(self):

        claves = ["tea", "production", "technique"]
        clavesAnalizar = analizador.analizar(claves)

        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")
        #self.assertIsNotNone(sinonimosClaves, "Analizador no debe lanzar None")