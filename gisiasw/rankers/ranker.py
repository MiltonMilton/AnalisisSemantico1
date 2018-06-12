from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager
from gisiasw.algoritmos.Synonim import compareWords, getListaSinonimos
from gisiasw.scrapper.Scrapper import Scrapper
from pattern.text.en import singularize
from pattern.web import Google,plaintext

def contiene(word, listOfSentences):
    for sentence in listOfSentences:
        if word in sentence.lower().split(): return True
    return False

def contruirClaveCompuestaAND(claves):
    claveCompuestaAND = ""
    for indiceClave in range(len(claves) - 1):
        claveCompuestaAND = claves[indiceClave] + " AND " + claveCompuestaAND 
    claveCompuestaAND = claveCompuestaAND + " " + claves[len(claves) - 1]
    return claveCompuestaAND




#RANKER DE TOPIC MODELLING Y SIMILARITY
def ejecutar():
    analizador = AnalisisSemanticoManager()
    claves = ["tea","production","technique"]
    claves = [singularize(clave) for clave in claves]
    engine = Google(license="AIzaSyCvvHb8SYgHvS5gEIQabxuJ0Kl0sYdHl9U", language="en")
    claveCompuestaAND = contruirClaveCompuestaAND(claves)
    urls=[]
    for result in engine.search(claveCompuestaAND):
            urls.append(result.url)

    print "CLAVES DE BUSQUEDA: " + str(claves)
    print "COMBINACION CLAVES: " + str(claveCompuestaAND)

    valoraciones = []
    for url in urls:
            topicModel = analizador.procesarURL(url)[0]
            subtopic = str(topicModel.get("word"))
            subtopicPonderation = topicModel.get("ponderacion")
            for clave in claves:
                similaridad = compareWords(clave,subtopic)
                valoracionClave = similaridad * subtopicPonderation
                valoraciones.append({"url":url ,"clave": clave, "subtopico": subtopic,"ponderacion":subtopicPonderation,"similaridad": similaridad, "valoracion":valoracionClave})

    print("RANKER TOPIC MODELLING Y SIMILARITY")

    valoraciones = sorted(valoraciones, key=lambda k:k.get("valoracion"))
    for valoracion in valoraciones:
        print str(valoracion)  + "\n"

    valoraciones = []
    scrapper = Scrapper()

    for url in urls:
        listOfSentences = scrapper.buscarHTML("",url)
        for clave in claves:
            try:
                numerador = 0
                sinonimos = getListaSinonimos(clave)
                sinonimos = [str(word) for word in sinonimos]#de unicode a string
                for word in sinonimos:
                    if contiene(word,listOfSentences): numerador = numerador + 1
                denominador = len(sinonimos)
                if denominador != 0:
                    valoracionClave = float(numerador) / denominador
                else:
                    valoracion = float(0)
                valoraciones.append({"url":url,"clave":clave, "sinonimos":sinonimos,"valoracion":valoracionClave})
            except Exception as e:
                pass

    print("RANKER SINONIMOS")

    valoraciones = sorted(valoraciones, key=lambda k:k.get("valoracion"))
    for valoracion in valoraciones:
        print str(valoracion) + "\n"

