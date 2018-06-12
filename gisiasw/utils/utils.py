def contiene(word, listOfSentences):
    for sentence in listOfSentences:
        if word in sentence.lower().split(): return True
    return False

def contruirClaveCompuestaAND(claves):
    claveCompuestaAND = ""
    for indiceClave in range(len(claves) - 1):
        claveCompuestaAND = claves[indiceClave] + " AND " + claveCompuestaAND
    claveCompuestaAND = claveCompuestaAND + " " + claves[len(claves) - 1]
    return claveCompuestaAND
