from gisiasw.similaridad.similaridad import similitudPorAlgoritmo

class MatrixManager:

    def analizarClaveTopico(self, claves,csinonimos, topicos, metodo):

        m = []

        for l, t in enumerate(topicos):
            matriz = self.armarMatrixClaveTopicos(claves, t, metodo)
            matrizClaveSinonimoTopico = self.armarMatrixClaveSinonimosTopicos(claves, t, metodo)
            matrizSinonimoClaveTopico = self.armarMatrixSinonimosClaveTopicos(csinonimos, t, metodo)
            matrizSinonimoClaveSinonimoTopico = self.matrizSinonimoClaveSinonimoTopico(csinonimos, t, metodo)
            encabezadoTopicos = [topico.get("word") for j, topico in enumerate(t.get("topics"))]
            m.append({"url":t.get("url"),
                      "matriz": matriz,
                      "index": l + 1,
                      "topicos": encabezadoTopicos,
                      "matrizSinonimosTopicos":matrizClaveSinonimoTopico,
                      "matrizSinonimoClaveTopico":matrizSinonimoClaveTopico,
                      "matrizSinonimoClaveSinonimoTopico": matrizSinonimoClaveSinonimoTopico,
                      })
        print(m)
        return m

    def armarMatrixClaveTopicos(self, claves, t, metodo):
        matriz = []
        for i in range(0, len(claves)):
            matrizClaveTopico = []
            for j, topico in enumerate(t.get("topics")):
                matrizClaveTopico.append({
                    "clave": claves[i],
                    "topico": topico.get("word"),
                    "ponderacionTopico": topico.get("ponderacion"),
                    "similaridad": similitudPorAlgoritmo(claves[i], topico.get("word"))
                })
            matriz.append(matrizClaveTopico)

        return  matriz

    def armarMatrixClaveSinonimosTopicos(self, claves, t, metodo):
        matriz = []
        for i in range(0, len(claves)):
            matrizClaveTopico = []
            for j, topico in enumerate(t.get("topics")):
                matrizClaveSinonimo = []
                for k, sinonimo in enumerate(t.get("sinonimos")[j]):
                    matrizClaveSinonimo.append({
                        "clave": claves[i],
                        "topico": topico.get("word"),
                        "sinonimo": sinonimo,
                        "similaridad": similitudPorAlgoritmo(claves[i], sinonimo)
                    })
                matrizClaveTopico.append(matrizClaveSinonimo)

            matriz.append(matrizClaveTopico)

        return  matriz

    def armarMatrixSinonimosClaveTopicos(self, claves, t, metodo):
        matriz = []
        for z, sinonimosClave in enumerate(claves):
            sinonimosClaveMatrix = []
            for i in range(0, len(sinonimosClave)):
                matrizClaveTopico = []
                for j, topico in enumerate(t.get("topics")):
                    matrizClaveTopico.append({
                        "clave": sinonimosClave[i],
                        "topico": topico.get("word"),
                        "ponderacionTopico": topico.get("ponderacion"),
                        "similaridad": similitudPorAlgoritmo(sinonimosClave[i], topico.get("word"))
                    })
                sinonimosClaveMatrix.append(matrizClaveTopico)
            matriz.append(sinonimosClaveMatrix)

        return  matriz

    def matrizSinonimoClaveSinonimoTopico(self, claves, t, metodo):
        matriz = []
        for z, sinonimosClave in enumerate(claves):
            SinonimosClaveSinonimosTopicos = []
            for i in range(0, len(sinonimosClave)):
                matrizClaveTopico = []
                for j, topico in enumerate(t.get("topics")):
                    matrizClaveSinonimo = []
                    for k, sinonimo in enumerate(t.get("sinonimos")[j]):
                        matrizClaveSinonimo.append({
                            "clave": sinonimosClave[i],
                            "topico": topico.get("word"),
                            "sinonimo": sinonimo,
                            "similaridad": similitudPorAlgoritmo(sinonimosClave[i], sinonimo)
                        })
                    matrizClaveTopico.append(matrizClaveSinonimo)
                SinonimosClaveSinonimosTopicos.append(matrizClaveTopico)
            matriz.append(matrizClaveTopico)

        return  matriz