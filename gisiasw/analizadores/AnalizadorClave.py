from gisiasw.algoritmos.Synonim import getListaSinonimos
class AnalizadorClave:

    def analizar(self, claves):

        clavesAnalizar = []
        sinonimosClaves = []
        for i,clave in enumerate(claves):
            clavesAnalizar.append(clave)
            sinonimosClaves.append(getListaSinonimos(clave))

        return clavesAnalizar, sinonimosClaves
