from gisiasw.algoritmos.Synonim import compareWords, getListaSinonimos

def claveTopico(claves, topicos):
    result = []
    for i in range(len(claves)):
        clavextopico = []
        for j in range(len(topicos)):
            clavextopico.append({
                "clave":claves[i],
                "topico": topicos[j],
                "compare": compareWords(claves[i], topicos[j])
            })

        result.append(clavextopico)

    return result
