import textrazor

class EntityRecognizer:

    def recognize(self,url):
        textrazor.api_key = "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze_url(url)
        entities = []
        for entity in response.entities():
            if entity.relevance_score > 0.75: entities.append(entity.id)
        return list(set(entities))[:5] #elimina duplicados y toma los primeros 5