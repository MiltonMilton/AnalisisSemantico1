from gisiasw.pruebasCongreso.searcher import Searcher
from gisiasw.scrapper.Scrapper import Scrapper
import spotlight

GOOGLE = "google"
BING = "bing"
searcher = Searcher()
scrapper = Scrapper()

class CongresoManager:
    def initialize(self, engine, keys):
        resultados = []
        #Por cada key, busco en el engine que paso como parametro
        #una lista de urls. Cada url la de debo scrapear y extraer
        #el contenido, y pasar por el reconocedor de entidades.
        urls_engine = searcher.search(keys=keys, engine=engine, n=10)
        for url in enumerate(urls_engine):
            content = self.get_conceptos(url[1])


        return resultados

    def get_content(self, url):
        return scrapper.buscarHtmlCompleto(url=url)

    def get_conceptos(self, url):
        import textrazor
        textrazor.api_key = "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze_url(url=url)
        entities = []
        for entity in response.entities():
            print entity.id, entity.relevance_score, entity.confidence_score, entity.freebase_types
            #print "entidad: " + str(entity.id)
            #print "relevancia: " + str(entity.relevance_score)
            #print "tipos: " + str(entity.freebase_types)
            #print("Entity" + entity)
            print ("__________________________________ ")