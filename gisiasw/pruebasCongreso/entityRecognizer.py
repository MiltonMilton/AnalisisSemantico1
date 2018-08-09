import textrazor
from nltk.corpus import wordnet as wn
from sematch.semantic.similarity import EntitySimilarity
sim = EntitySimilarity()

#500 requests diarios cada key

keya="a6ccb809d4fe98c43b3492548298edf0b7d4ceb67aea9c58930eacc9"
keyb="8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
key = keya #aca seleccionas la llave


class EntityRecognizer:

    def recognizeSinFiltrar(self,url): #reconoce todas las entidades
        import operator


        textrazor.api_key = keyb#"9ef66800304909b23755c07c8cffda50a1f4bfc2462327c32d3b65d7"
        client = textrazor.TextRazor(extractors=["entities", "topics", "relations"])
        words = client.analyze("machine learning python algorithms")
        response = client.analyze_url(url)

        #for entity in response.topics():
            #print(entity.label, entity.score)

        entities = []
        for entity in response.entities():
            print(entity.wikipedia_link, entity.document_id)
            if entity.relevance_score > 0.75:
                entities.append({
                    "entidad":entity.id.replace(" ", "_"),
                    "relevance":entity.relevance_score,
                    "long_name":entity.id,
                    "wiki": entity.dbpedia_types
                })

        newlist = sorted(entities, key=lambda k: k['relevance'], reverse=False)

        distinct_list = {x['entidad']: x for x in newlist}.values()

        distinct_list = sorted(distinct_list, key=lambda k: k['relevance'], reverse=True)

        return distinct_list[:10]

    def recognizeFirstFive(self,url): #reconoce las primeras 5 entidades cuyo umbral > 0.75
        textrazor.api_key =  key
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        response = client.analyze_url(url)
        entities75 = []
        entities50 = []
        entities20 = []
        for entity in response.entities():
            if entity.relevance_score > 0.75: entities75.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
            if entity.relevance_score > 0.50: entities50.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
            if entity.relevance_score > 0.20: entities20.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
        if len(list(set(entities75))) > 4: return list(set(entities75))[:5]       
        elif len(list(set(entities50))) > 4: return list(set(entities50))[:5]
        else: return list(set(entities20))[:5]    

    def recognizeAndCheckSynset(self,url):
        #reconoce las primeras 5 entidades 
        #que existan y wordnet y tengan el mayor score posible


        #MILTON_API_KEY= "8cdcb70d8ae86e21ac318e3d8cd6fb2b456f6e9f984d39267fa78d32"
        #MANU_API_KEY = "9ef66800304909b23755c07c8cffda50a1f4bfc2462327c32d3b65d7"
        textrazor.api_key = key


        client = textrazor.TextRazor(extractors=["entities", "topics"])
        client.set_cleanup_mode("cleanHTML")
        client.set_classifiers(["textrazor_mediatopics"])
        response = client.analyze_url(url)

        entities = []
        entities95 = []
        entities75 = []
        entities50 = []
        entities40 = []
        print(response.entities())
        if len(list(set(response.entities()))) == 0: return entities
        for entity in list(set(response.entities())):
            print(entity.id, entity.dbpedia_types)
            if entity.relevance_score > 0.95: entities95.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
            if entity.relevance_score > 0.75 and entity.relevance_score <=0.95: entities75.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
            if entity.relevance_score > 0.50 and entity.relevance_score <=0.75: entities50.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
            if entity.relevance_score > 0.40 and entity.relevance_score <=0.50: entities40.append({"Entidad":entity.id, "Relevance Score":entity.relevance_score})
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

    def recognizeAndCheckSynset2(self,url):
        #set client
        textrazor.api_key = key
        client = textrazor.TextRazor(extractors=["entities", "topics"])
        client.set_cleanup_mode("cleanHTML")
        client.set_classifiers(["textrazor_mediatopics"])
        response = client.analyze_url(url)
        #get entities
        entities = []
        aux = []
        if len(list(set(response.entities()))) == 0: return entities
        for entity in list(set(response.entities())):
            if (wn.synsets(entity.id) <> []):
                aux.append(entity.id)
                aux = list(set(aux))
                if len(aux) > len(entities):
                    entities.append(entity)
        return sorted(entities, key=lambda entity: entity.relevance_score, reverse =True) 
            



         

