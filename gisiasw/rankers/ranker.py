from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager
from gisiasw.algoritmos.Synonim import compareWordsSinonimos, synsetSinonimo, getListaSinonimos
from gisiasw.scrapper.Scrapper import Scrapper

def count_occurrences(word, listOfSentences):
    ocurrencias = 0
    for sentence in listOfSentences:
        ocurrencias = ocurrencias + (sentence.lower().split().count(word))
    return ocurrencias

#RANKER DE TOPIC MODELLING Y SIMILARITY

analizador = AnalisisSemanticoManager()
claves = ["dog","white","car","fruit","inmigrants"]
url = "https://simple.wikipedia.org/wiki/Banana"
#"http://www.bbc.com/news/health-44338276"

for i in analizador.procesarURL(url):
    print i
    print("RANKER TOPIC MODELLING Y SIMILARITY")
    subtopic = i.get("word") 
    subtopicPonderation = i.get("ponderacion")

    valoraciones = []

    for clave in claves:
            
        # try:
            try:
                similaridad = compareWordsSinonimos(clave,subtopic)
                valoracionClave = similaridad * subtopicPonderation
                valoraciones.append({"clave": clave, "subtopico": subtopic, "valoracion": valoracionClave})
            except Exception as e:
                pass
            
            for valoracion in valoraciones:
                print "clave: " + valoracion.get("clave") + ";  subtopico: " + valoracion.get("subtopico")+ "; valoracion: " + str(valoracion.get("valoracion"))
                print("")
            

        # except Exception as e:
        #     print "synset clave vacio:" + str(synsetSinonimo(clave) == []) 
        #     print "synset subtopic vacio:" + str(synsetSinonimo(subtopic) == []) 
        # pass

#RANKER DE SINONIMOS


valoraciones = []

scrapper = Scrapper()
listOfSentences = scrapper.buscarHTML("",url)
for clave in claves:
    try:
        numerador = 0
        for sinonimo in getListaSinonimos(clave):
            numerador = numerador + (count_occurrences(sinonimo,listOfSentences))
        #CORREGIR VER DOCUMENTO: BORRADOR METRICAS EN DRIVE
        denominador = len(getListaSinonimos(clave))
        valoracionClave = numerador
        valoraciones.append({"clave":clave,"valoracion":valoracionClave})
    except Exception as e:
        pass  

print("RANKER SINONIMOS")
for valoracion in valoraciones:
    print valoracion
    print(" ")


