from SPARQLWrapper import SPARQLWrapper, JSON

def get_graph(entity,levels):
    grafo = []
    already_expanded = []
    entities = []
    entities.append(entity)
    for i in range(levels): #no uso el indice
        grafo,entities,already_expanded = get_graph_level(grafo,entities,already_expanded)
    return grafo



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
                aux.append({"nombre":node,"relacion":-1}) #broader se representa con -1
            for node in subjects:
                aux.append({"nombre":node,"relacion": 1}) #subject se representa con  1
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

#testEntity = "Support_vector_machine"
