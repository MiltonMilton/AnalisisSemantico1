import unittest
import gisiasw.scrapper.Scrapper as sc


class TestScrapper(unittest.TestCase):

    def test_html_string(self):

        self.assertTrue(type(sc.Scrapper.buscarHTML(self, 'prueba','./ejemplo.html')) == str, 'La salida del scrapper debe ser un string')

  