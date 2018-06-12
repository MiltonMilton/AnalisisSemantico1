from pattern.text import singularize
from pattern.web import Google
from gisiasw.scrapper.Scrapper import Scrapper
from gisiasw.utils.utils import contruirClaveCompuestaAND
from gisiasw.algoritmos.TopicModeling import TopicModeling
from gisiasw.algoritmos.Synonim import getListaSinonimos

class AnalizadorTopicos:
    scrapper = Scrapper()

    def analizar(self, claves):
        #Busco en Pattern los recursos
        urls = self.analizar_recursos(claves)
        print("TENGO URLS:", urls)
        #analizo el contenido de los documentos
        topics = self.analizar_url(urls)
        #aplico TopicModeling
        #Extraigo los topicos mas relevantes
        sinonimosTopicos = self.getSinonimos(topics)
        #busco los sinonimos de cada topico
        return topics, sinonimosTopicos

    def analizar_recursos(self, claves):
        claves = [singularize(clave) for clave in claves]
        engine = Google(license="AIzaSyCvvHb8SYgHvS5gEIQabxuJ0Kl0sYdHl9U", language="en")
        claveCompuestaAND = contruirClaveCompuestaAND(claves)
        urls = []
        for result in engine.search(claveCompuestaAND):
            urls.append(result.url)

        return urls

    def analizar_url(self, urls):
        tp = TopicModeling()
        topics = []
        texts = []
        for i, url in enumerate(urls):
            print("BUSCO URL", url)
            texts.append(self.scrapper.buscarHtmlCompleto(url))

        topics = tp.analizar(texts)

        print(topics)

        return topics

    def getSinonimos(self, topics):
        sinonimosXTopics = []
        for i,topic in enumerate(topics):
            sinonimosXTopics.append(getListaSinonimos(topic.get("word")))

        print(sinonimosXTopics)

        return sinonimosXTopics