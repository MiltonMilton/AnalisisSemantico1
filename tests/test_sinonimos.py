import unittest

from gisiasw.algoritmos.Synonim import getSinonimo, compareWords

class Test_Sinonimo(unittest.TestCase):

    def test_get_sinonimo(self):
        palabra = "good"
        estructura = getSinonimo(palabra)
        self.assertIsNotNone(estructura)

        print(compareWords("area","leather"))
        self.assertIsNotNone(compareWords("leather", "area"))