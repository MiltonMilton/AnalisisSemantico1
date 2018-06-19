from gisiasw.similaridad.similaridad import similaridad

class MatrixManager:

    def analizarClaveTopico(self, claves, topicos, metodo):

        m = []
        for i in range(0, len(claves)):
            matrizClaveTopico = []
            for j,topico in enumerate(topicos):
                matrizClaveTopico.append({
                    "clave":claves[i],
                    "topico": topico.get("word"),
                    "ponderacionTopico":topico.get("ponderacion"),
                    "similaridad":similaridad(claves[i], topico.get("word"), metodo),
                    "fila": i+1,
                    "columna": j+1
                })
            m.append(matrizClaveTopico)

        print(m)
        return m