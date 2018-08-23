from SPARQLWrapper import SPARQLWrapper, JSON

def get_graph(entity,levels):
    grafo = []
    already_expanded = []
    entities = []
    entities.append(entity)
    for i in range(levels): #no uso el indice
        grafo,entities,already_expanded = get_graph_level(grafo,entities,already_expanded)
    return grafo

def dke(key,entity):
    levs = get_entities_by_level(key,levels = 5)
    for level in levs.keys():
        if entity in levs[level]:
            return level
    return -1

def dke2(levs,entity): #se le pasa el grafo en vez de la key, para no construirlo todas las veces
    for level in levs.keys():
        if entity in levs[level]:
            return level
    return -1

def get_entities_by_level(entity,levels):#retorna una lista donde se muestran las entites de cada nivel
    grafo = []
    already_expanded = []
    entities = []
    entitiesByLevel = {}
    entities.append(entity)
    for i in range(levels): #no uso el indice
        entitiesByLevel[i]= entities 
        grafo,entities,already_expanded = get_graph_level(grafo,entities,already_expanded)
    return entitiesByLevel

def get_entities_by_level_sin_acumular(entity,levels):#retorna una lista donde se muestran las entites de cada nivel
    grafo = []
    already_expanded = []
    entities = []
    entitiesByLevel = {}
    entities.append(entity)
    for i in range(levels): #no uso el indice
        if i == 0:
            entitiesByLevel[i] = entities
        else:
            aux = []
            for lev in entitiesByLevel.keys():
                aux = aux + entitiesByLevel[lev]
            entitiesByLevel[i] = entities
            entitiesByLevel[i] = list(set(entitiesByLevel[i])-set(aux))
        grafo,entities,already_expanded = get_graph_level(grafo,entities,already_expanded)
    return entitiesByLevel



def get_graph_level(grafo,entities,already_expanded_in):
    
    subjects= []
    broaders = []
    aux2 = []
    aux3 = []
    for entity in entities:
        
        aux2 = []
        if entity not in already_expanded_in:
            for e in get_subjects(entity):
                subjects.append(e)
            for e in get_broaders(entity):
                broaders.append(e)
            aux = []
            for node in broaders:
                aux.append(node)
            for node in subjects:
                aux.append(node)
            grafo.append({entity:aux})
            aux2 = list(set(subjects + broaders))
            aux3 = aux2 + aux3
    already_expanded_out = list(set(already_expanded_in + entities))
    entities = list(set(entities + aux3))
    
    return grafo,entities, already_expanded_out

def get_subjects(entity):
    query = """
        SELECT ?subject
        WHERE { 
            <http://dbpedia.org/resource/"""+entity+"""> dct:subject ?subject
        }
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs = []

    for result in results["results"]["bindings"]:
        cs.append(result["subject"]["value"].split(":")[2])
    return cs

def get_broaders(entity):
    query = """
        SELECT ?broader
        WHERE { 
            <http://dbpedia.org/resource/Category:"""+entity+"""> skos:broader ?broader
        }
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs = []

    for result in results["results"]["bindings"]:
        cs.append(result["broader"]["value"].split(":")[2])
    return cs
