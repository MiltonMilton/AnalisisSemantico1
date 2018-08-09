rs = []
def build_graph(concept, key=None, counter=0, k=0, name=None):
    concepts = get_concepts_From_dbpedia(concept)
    counter = 0
    rs.append({
        name: [z["type"] for z in concepts]
    })
    build_graph_p(concepts)
    return  rs
    print(rs)

def build_graph_p(concepts):
    for k,c in enumerate(concepts):
        l =  get_subject_From_dbpedia(c.get("cat_link"))
        rs.append({
            c.get("type"):[z["type"] for z in l]
        })



def get_concepts_From_dbpedia(concept):
    from SPARQLWrapper import SPARQLWrapper, JSON
    query = """
        PREFIX dct:  <http://purl.org/dc/terms/> 
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?subject
        WHERE { 
            <"""+concept+"""> dct:subject ?subject            
        }
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs = []
    for result in results["results"]["bindings"]:
        cs.append({
            "type": result["subject"]["value"].split(":")[2],
            "cat_link":result["subject"]["value"]
        })

    return cs

def get_subject_From_dbpedia(concept):
    print(concept)
    from SPARQLWrapper import SPARQLWrapper, JSON
    query = """
        SELECT ?broader
        WHERE { 
            <"""+concept+"""> skos:broader ?broader
        }
    """
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query=query)

    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    cs = []
    print(results)
    for result in results["results"]["bindings"]:
        cs.append({
            "type": result["broader"]["value"].split(":")[2],
            "cat_link":result["broader"]["value"]
        })

    return cs

build_graph("http://dbpedia.org/resource/Support_vector_machine", name="Support_vector_machine")