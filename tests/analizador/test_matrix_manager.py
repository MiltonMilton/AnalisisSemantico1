#[{'word': u'tea', 'ponderacion': 0.051252183}, {'word': u'leaf', 'ponderacion': 0.014983851}, {'word': u'green', 'ponderacion': 0.006618309}, {'word': u'process', 'ponderacion': 0.0061947373}, {'word': u'dry', 'ponderacion': 0.004818129}, {'word': u'roll', 'ponderacion': 0.0039709853}, {'word': u'production', 'ponderacion': 0.0035474135}, {'word': u'use', 'ponderacion': 0.0035474135}, {'word': u'method', 'ponderacion': 0.0034415207}, {'word': u'_', 'ponderacion': 0.0032297347}]

import unittest
from gisiasw.managers.MatrixManager import MatrixManager

matriz = MatrixManager()
class TestAnalizadorTopicos(unittest.TestCase):


    def test_analizador_con_metodo_lch(self):

        topicos = [{'word': u'tea', 'ponderacion': 0.051252183}, {'word': u'leaf', 'ponderacion': 0.014983851}, {'word': u'green', 'ponderacion': 0.006618309}, {'word': u'process', 'ponderacion': 0.0061947373}, {'word': u'dry', 'ponderacion': 0.004818129}, {'word': u'roll', 'ponderacion': 0.0039709853}, {'word': u'production', 'ponderacion': 0.0035474135}, {'word': u'use', 'ponderacion': 0.0035474135}, {'word': u'method', 'ponderacion': 0.0034415207}, {'word': u'_', 'ponderacion': 0.0032297347}]
        claves = ["tea", "production", "technique"]

        clavesAnalizar = matriz.analizarClaveTopico(claves, topicos, "lch")

        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")

    def test_analizador_con_metodo_path(self):

        topicos = [{'word': u'tea', 'ponderacion': 0.051252183}, {'word': u'leaf', 'ponderacion': 0.014983851}, {'word': u'green', 'ponderacion': 0.006618309}, {'word': u'process', 'ponderacion': 0.0061947373}, {'word': u'dry', 'ponderacion': 0.004818129}, {'word': u'roll', 'ponderacion': 0.0039709853}, {'word': u'production', 'ponderacion': 0.0035474135}, {'word': u'use', 'ponderacion': 0.0035474135}, {'word': u'method', 'ponderacion': 0.0034415207}, {'word': u'_', 'ponderacion': 0.0032297347}]
        claves = ["tea", "production", "technique"]

        clavesAnalizar = matriz.analizarClaveTopico(claves, topicos, "path")

        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")

    def test_analizador_con_metodo_wup(self):
        topicos = [{'word': u'tea', 'ponderacion': 0.051252183}, {'word': u'leaf', 'ponderacion': 0.014983851},
                   {'word': u'green', 'ponderacion': 0.006618309}, {'word': u'process', 'ponderacion': 0.0061947373},
                   {'word': u'dry', 'ponderacion': 0.004818129}, {'word': u'roll', 'ponderacion': 0.0039709853},
                   {'word': u'production', 'ponderacion': 0.0035474135}, {'word': u'use', 'ponderacion': 0.0035474135},
                   {'word': u'method', 'ponderacion': 0.0034415207}, {'word': u'_', 'ponderacion': 0.0032297347}]
        claves = ["tea", "production", "technique"]

        clavesAnalizar = matriz.analizarClaveTopico(claves, topicos, "wup")

        self.assertIsNotNone(clavesAnalizar, "Analizador no debe lanzar None")

