import textrazor
from nltk.corpus import wordnet as wn


class EntityRecognizer:

    def recognizeSinFiltrar(self,url): #reconoce todas las entidades
        textrazor.api_key = "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze_url(url)
        entities = []
        for entity in response.entities():
            entities.append(entity.id)
        return list(set(entities)) 

    def recognizeFirstFive(self,url): #reconoce las primeras 5 entidades cuyo umbral > 0.75
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

    def recognizeAndCheckSynset(self,url):
        #reconoce las primeras 5 entidades 
        #que existan y wordnet y tengan el mayor score posible
        textrazor.api_key = "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"

        client = textrazor.TextRazor(extractors=["entities", "topics"])
        client.set_cleanup_mode("cleanHTML")
        client.set_classifiers(["textrazor_mediatopics"])
        response = client.analyze_url(url)
        entities = []
        entities95 = []
        entities75 = []
        entities50 = []
        entities40 = []
        if len(list(set(response.entities()))) == 0: return entities
        for entity in list(set(response.entities())):
            if entity.relevance_score > 0.95: entities95.append(entity.id)
            if entity.relevance_score > 0.75 and entity.relevance_score <=0.95: entities75.append(entity.id)
            if entity.relevance_score > 0.50 and entity.relevance_score <=0.75: entities50.append(entity.id)
            if entity.relevance_score > 0.40 and entity.relevance_score <=0.50: entities40.append(entity.id)
        c = 5 #cantidad de entidades pendientes
        entitiesLists = []
        entitiesLists.append(entities95)
        entitiesLists.append(entities75)
        entitiesLists.append(entities50)
        entitiesLists.append(entities40)
        resguardo = []
        i = 0 #indice array
        while c > 0:
            if i < len(entitiesLists):
                if entitiesLists != []:
                    for entity in entitiesLists[i]:
                        if len(wn.synsets(entity)) > 0:
                            resguardo = entities 
                            entities.append(entity)
                            entities = list(set(entities))
                            if len(entities) > len(resguardo):
                                c = c - 1
                i = i + 1
            else:
                return entities[:5] 
        return entities[:5] 
         

