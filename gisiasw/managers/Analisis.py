from gisiasw.analizadores.AnalizadorClave import AnalizadorClave
from gisiasw.analizadores.AnalizadorTopicos import AnalizadorTopicos
from gisiasw.managers.MatrixManager import MatrixManager
class Analisis:

    matrix = MatrixManager()
    analisisClave = AnalizadorClave()
    analisisTopico = AnalizadorTopicos()

    def armarMatrizdeSimilitudes(self, claves, metodo):
        #busco los sinonimos de claves
        claves, csinonimos = self.analisisClave.analizar(claves)
        #busco los topicos y sus sinonimos
        topicos, ctopicos = self.analisisTopico.analizar(claves)
        #construyo la matriz
        matriz = self.matrix.analizarClaveTopico(claves, topicos, "lch")
        #armo los encabezados
        encabezadoTopicos =  [topico.get("word") for j, topico in enumerate(topicos)]
        #retorno la matriz

        return {
                "claves": claves,
                "topicos": encabezadoTopicos,
                "matriz": matriz
        }

