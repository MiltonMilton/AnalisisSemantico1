
def format(words):
    formatted_data = []
    edges = []
    grupo = 0
    ids = 1
    
    for i in range(len(words)):
        palabra = words[i]
        sinonimos = palabra.get('sinonimos')
        formatted_data.append({
            "id": ids,
            "label": palabra.get('tipo')+ ": - " +palabra.get('word'),
            "group": i
        })

        for j in range(len(words[i].get('sinonimos'))):
            ids += 1
            sinonimo = sinonimos[j]
            formatted_data.append({
                "id": ids,
                "label": "SINONIMO:" + sinonimo.get('tipo') + ": - " + sinonimo.get('word'),
                "group": i
            })
            edges.append({
                "from": ids,
                "to": i
            })


    for j in range(len(formatted_data)):
        print(formatted_data[j].get('id'))

    return  formatted_data, edges