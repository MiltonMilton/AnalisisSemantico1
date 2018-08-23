import xlsxwriter
from simpleGraphGenerator import get_entities_by_level_sin_acumular as gebl
from simpleGraphGenerator import dke2 as dke
#busquedas
from gisiasw.pruebasCongreso.searcher import Searcher
#textrazor
from gisiasw.pruebasCongreso.entityRecognizer import EntityRecognizer

#inicializamos documentos

workbook = xlsxwriter.Workbook("pruebaCongreso.xlsx")
google_sheet = workbook.add_worksheet()
bing_sheet = workbook.add_worksheet()

keys = ["Support_vector_machine","tutorial"] #lo idea es que las keys sean entities de dbpedia

#busqueda
s = Searcher()
n = 20
google_results = s.search(keys,"google",n) #resultados google
bing_results = s.search(keys,"bing",n) #resultados bing

grafos = []

#generar grafos de las keys por niveles (N niveles, desde nivel 0 a nivel N-1)
N = 6
for key in keys:
    print "generando grafo de: " + str(key)
    grafos.append(gebl(key,N))

#funcion que realiza las hojas

def escribir_hoja(grafos,results,worksheet):
    row = 0
    col = 0
    #el documento se va escribiendo por filas (rows)
    for result in results:
        entity_recognizer = EntityRecognizer()
        entities = entity_recognizer.recognizeFirst5(result)
        #remplazamos los espacios blancos por underscores para encontrarlos en los grafos
        entities_ = []
        for entity in entities:
            entities_.append(str(entity).replace(" ","_"))
        print entities_
        #recurso
        print "analizando recurso: " + str(result)  
        worksheet.write(row,0,str(result))
        row += 1  
        #escribimos las entities reconocidas en el recurso
        for entity in entities_:
            col += 1
            worksheet.write(row,col,entity)
        #construimos los vectores con las metricas
        for grafo in grafos:
            #salto de linea, es decir, row += 1, col = 0
            row += 1
            col = 0
            worksheet.write(row,col,str(grafo[0][0])) #imprimimos la key
            for entity in entities_:
                col += 1
                worksheet.write(row,col,dke(grafo,entity))
        #siguiente recurso
        row += 2
        col = 0

#realizacion de la prueba    

escribir_hoja(grafos,google_results,google_sheet)
escribir_hoja(grafos,bing_results,bing_sheet)

#guardamos archivo

workbook.close()            

            


