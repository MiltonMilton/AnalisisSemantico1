
from SPARQLWrapper import SPARQLWrapper, JSON

class DBPedia:

    def getData(self):
        print("INICIANDO PROCESAMIENTO")
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        sparql.setQuery("""
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>        
            PREFIX type: <http://dbpedia.org/class/yago/>
            PREFIX prop: <http://dbpedia.org/property/>
            SELECT ?lbl ?est
            WHERE {
              ?country rdfs:label ?lbl .
              FILTER(bif:contains(?lbl, "Republic")) .
              ?country a type:Country108544813 ;
                  prop:establishedDate ?est .
              FILTER(?est < "1920-01-01"^^xsd:date) .
            }
    
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        print(results)

        for result in results["results"]["bindings"]:
            print(result["label"]["value"])

        return None