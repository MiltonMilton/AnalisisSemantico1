from gisiasw.analizadores.AnalizadorClave import AnalizadorClave
from gisiasw.analizadores.AnalizadorTopicos import AnalizadorTopicos
from gisiasw.managers.MatrixManager import MatrixManager
class Analisis:

    matrix = MatrixManager()
    analisisClave = AnalizadorClave()
    analisisTopico = AnalizadorTopicos()

    def armarMatrizdeSimilitudes(self, claves, metodo, urls):
        #busco los sinonimos de claves
        cclaves, csinonimos = self.analisisClave.analizar(claves)
        #busco los topicos y sus sinonimos
        topicos, ctopicos = self.analisisTopico.analizar(claves) if len(urls) == 0 else self.analisisTopico.analizar_con_urls(urls)
        #construyo la matriz
        matriz = self.matrix.analizarClaveTopico(claves, topicos, metodo)
        #armo los encabezados
        encabezadoTopicos =  [topico.get("word") for j, topico in enumerate(topicos)]
        #retorno la matriz

        return {
                "claves": cclaves,
                "topicos": encabezadoTopicos,
                "matriz": matriz
        }

