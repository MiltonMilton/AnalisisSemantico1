import unittest
from gisiasw.scrapper.Scrapper import Scrapper
scrapper = Scrapper()

class TestScrapper(unittest.TestCase):


    def test_get_content(self):

        content = scrapper.buscar("Google", "http://www.django-rest-framework.org/?q=migrations")
        print(content)
        self.assertIsNotNone(content, "Content should not be empty")