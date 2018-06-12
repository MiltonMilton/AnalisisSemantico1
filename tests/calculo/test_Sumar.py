import unittest
import gisiasw.calculo.suma


class TestSumar(unittest.TestCase):

    def test_sumar_dos_numeros(self):

        self.assertEqual(4, gisiasw.calculo.suma.sumar(2, 2), "La suma debe ser 4")

    def test_sumar_un_numero_tipo_entero_con_un_string(self):

        self.assertRaises(TypeError, gisiasw.calculo.suma.sumar, 2, "2", "No debe ser 4")
