from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager
from gisiasw.algoritmos.Synonim import compareWords, getListaSinonimos
from gisiasw.scrapper.Scrapper import Scrapper
from pattern.text.en import singularize




def contiene(word, listOfSentences):
    for sentence in listOfSentences:
        if word in sentence.lower().split(): return True
    return False

#RANKER DE TOPIC MODELLING Y SIMILARITY

analizador = AnalisisSemanticoManager()
claves = ["dog","white","car","fruit","inmigrants"]
claves = [singularize(clave) for clave in claves]
print claves
url = "https://www.bbc.com/news/world-us-canada-44374756?intlink_from_url=https://www.bbc.com/news/topics/c302m85qe1vt/uk-immigration&link_location=live-reporting-story"
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
        for word in getListaSinonimos(clave):
            if contiene(word,listOfSentences): numerador = numerador + 1
        denominador = len(getListaSinonimos(clave)) #esta lista no contiene duplicados
        if denominador != 0: 
            valoracionClave = float(numerador) / denominador 
        else: 
            valoracion = float(0)
        valoraciones.append({"clave":clave,"valoracion":valoracionClave})
    except Exception as e:
        pass  

print("RANKER SINONIMOS")
for valoracion in valoraciones:
    print str(valoracion) + "\n"
    


