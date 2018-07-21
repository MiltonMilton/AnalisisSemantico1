from google import google 
#pip install Google-Search-API
#https://github.com/abenassi/Google-Search-API

def listToString(lista):
        string = ''
        for word in lista:
            string = string + ' ' + str(word)
        return string

class Searcher:

    def search(self,keys,n, engine):
        """
        keys: lista de strings
        n: cantidad de resultados
        engine: google o bing
        """
        urls = []
        if engine == "google":
            num_page = 5 
            search_results = google.search(listToString(keys), num_page)
            for result in search_results:
                urls.append(result.link)
            urls = urls[:n]
        elif engine == "bing":
            print "no implementado"
        else:
            print "invalid engine, use google or bing" 
            return urls
        return urls
