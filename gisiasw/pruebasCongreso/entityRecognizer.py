import textrazor

class EntityRecognizer:

    def recognize(self,url):
        textrazor.api_key = "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze_url(url)
        entities75 = []
        entities50 = []
        entities20 = []
        for entity in response.entities():
            if entity.relevance_score > 0.75: entities75.append(entity.id)
            if entity.relevance_score > 0.50: entities50.append(entity.id)
            if entity.relevance_score > 0.20: entities20.append(entity.id)
        if len(list(set(entities75))) > 4: return list(set(entities75))[:5]       
        elif len(list(set(entities50))) > 4: return list(set(entities50))[:5]
        else: return list(set(entities20))[:5]    