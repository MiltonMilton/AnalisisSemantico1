import unittest

from gisiasw.algoritmos.Synonim import getSinonimo, compareWords
from gisiasw.rankers.ranker import ejecutar
class Test_Sinonimo(unittest.TestCase):

    def test_get_sinonimo(self):
        palabra = "good"
        estructura = getSinonimo(palabra)
        self.assertIsNotNone(estructura)

        print(compareWords("tea","powder"))
        #print(ejecutar())
        self.assertIsNotNone(compareWords("leather", "area"))




