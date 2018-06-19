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
        topicos = self.analisisTopico.analizar_con_urls(urls)
        #construyo la matriz
        matrices = self.matrix.analizarClaveTopico(cclaves, csinonimos, topicos, metodo)
        #armo los encabezados

        #retorno la matriz

        return {
                "claves": cclaves,
                "matrices": matrices
        }

