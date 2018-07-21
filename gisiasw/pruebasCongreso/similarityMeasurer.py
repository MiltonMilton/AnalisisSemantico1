from gisiasw.similaridad.similaridad import similaridad

class SimilarityMeasurer:

    def measure(self, word, entity):
        medidas = []
        medidas.append(similaridad(word,entity,"wup"))
        medidas.append(similaridad(word,entity,"sde"))
        medidas.append(similaridad(word,entity,"lin"))
        medidas.append(similaridad(word,entity,"path"))
        return medidas

