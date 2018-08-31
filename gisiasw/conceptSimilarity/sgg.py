from SPARQLWrapper import SPARQLWrapper, JSON

def get_graph(entity,levels):
    grafo = []
    already_expanded = []
    entities = []
    entities.append(entity)
    for i in range(levels): #no uso el indice
        grafo,entities,already_expanded = get_graph_level(grafo,entities,already_expanded)
    return grafo

# def dke_(key,entity):
#     levs = get_entities_by_level(key,levels = 5)
#     for level in levs.keys():
#         if entity in levs[level]:
#             return level
#     return -1

def dke_niveles(niveles_de_grafo,entity): #se le pasa niveles_de_grafo en vez de la key, para no construirlo todas las veces
    for level in niveles_de_grafo.keys():
        if entity in niveles_de_grafo[level]:
            return level
    return -1


def get_entities_by_level(entity,levels):#retorna una lista donde se muestran las entites de cada nivel
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
        print "generando nivel: " + str(i)
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
            print "expandiendo nivel para la entidad: " + entity
            aux = get_subjects(entity)
            grafo.append({entity: aux})
            aux3 = aux
    already_expanded_out = list(set(already_expanded_in + entities))
    entities = concat_arrays([entities, aux3])
    
    return grafo,entities, already_expanded_out

def concat_arrays(arrays):
    result = []
    for i, arr in enumerate(arrays):
        for i, ar1 in enumerate(arr):
            result.append(ar1)

    return result

def get_subjects(entity):
    query = """
            PREFIX  skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX  dbc:  <http://dbpedia.org/resource/Category:>
            PREFIX  dct:  <http://purl.org/dc/terms/>
            PREFIX  dbr: <http://dbpedia.org/resource/>

            SELECT  distinct ?subject
            WHERE  {   
                    { SELECT  ?subject
                        WHERE   { ?subject dct:subject/skos:broader <http://dbpedia.org/resource/Category:""" + entity + """> }
                    }
                    UNION
                    { SELECT  ?subject
                        WHERE { <http://dbpedia.org/resource/Category:""" + entity + """> skos:broader  ?subject }
                    }
                    UNION
                    { SELECT  ?subject
                        WHERE { <http://dbpedia.org/resource/""" + entity + """> dct:subject  ?subject 
                        FILTER( regex(str(?subject), "^(?!http://dbpedia.org/resource/Category:""" + entity + """)"))
                    }
                }

            }
        """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)
    # print(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs = []

    for result in results["results"]["bindings"]:
        if (result["subject"]["value"].find("/Category:") == -1):
            cs.append(result["subject"]["value"].split("/resource/")[1])
        else:
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

    query = """
        SELECT ?broader
        WHERE { 
            ?broader skos:broader <http://dbpedia.org/resource/Category:"""+entity+"""> .
        }
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs2 = []

    for result in results["results"]["bindings"]:
        cs2.append(result["broader"]["value"].split(":")[2])

    return cs + cs2
