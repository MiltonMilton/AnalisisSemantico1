import unittest
from gisiasw.clientes.DBPedia import DBPedia
from gisiasw.clientes.Spotlight import SpotLight
from gisiasw.scrapper.Scrapper import Scrapper
dbpedia = DBPedia()
spotlight = SpotLight()
scrapper = Scrapper()

class TestDBPedia(unittest.TestCase):


    def test_dbpedia(self):

        self.assertIsNotNone(dbpedia.getData())

    def test_spotlight(self):

        text = scrapper.buscarHtmlCompleto("http://www.eurekamagazine.co.uk/design-engineering-features/ip-advice/patent-of-the-month-a-better-way-to-make-your-tea/163102/")
        print(text)
        res = spotlight.getResources(text={
            "text": text,
            "confidence": 0.5,
            "support": 50
        })

        print(res)
        self.assertIsNotNone(res)