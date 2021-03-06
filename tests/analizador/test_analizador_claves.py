import unittest
from gisiasw.analizadores.AnalizadorClave import AnalizadorClave

analizador = AnalizadorClave()

class TestAnalizador(unittest.TestCase):



    def test_analizador(self):

        claves = ["tea", "production", "technique"]
        clavesAnalizar, sinonimosClaves = analizador.analizar(claves)

        print(clavesAnalizar)
        print(sinonimosClaves)
        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")
        self.assertIsNotNone(sinonimosClaves, "Analizador no debe lanzar None")