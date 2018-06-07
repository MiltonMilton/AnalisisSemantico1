from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager
from gisiasw.algoritmos.Synonim import compareWords, synsetSinonimo, getListaSinonimos
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
valoraciones = []
for i in analizador.procesarURL(url):
    subtopic = i.get("word") 
    subtopicPonderation = i.get("ponderacion")
    for clave in claves:
        try:
            similaridad = compareWords(clave,subtopic)
            valoracionClave = similaridad * subtopicPonderation
            valoraciones.append({"clave": clave, "subtopico": subtopic, "valoracion": valoracionClave})
        except Exception as e:
            pass
print("RANKER TOPIC MODELLING Y SIMILARITY")        
for valoracion in valoraciones:
    print str(valoracion)  + "\n"            

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
    print str(valoracion) + "\n"
    


