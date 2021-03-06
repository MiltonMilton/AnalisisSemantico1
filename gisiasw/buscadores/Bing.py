# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import os
import sys; sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from pattern.web import Bing, asynchronous, plaintext, URL  , SEARCH , time
import bs4 as bs
import urllib2

def generar_consulta_bing(q):
    reload(sys)
    sys.setdefaultencoding('utf8')

    engine_bing = Bing(license="TNMHm68dvf440pSPdnU+2LqxeQi7J2xszPZLBiPYsmI", language="en")
    bing = []
    for consulta in q:
        request = asynchronous(engine_bing.search, consulta, start=1, count=10, type=SEARCH, timeout=10)

        while not request.done:
            time.sleep(0.01)

        # An error occured in engine.search(), raise it.
        if request.error:
            raise request.error

        # Retrieve the list of search results.
        for result in request.value:
            bing.append(result.url)

    return bing


# Metodo que utiliza la libreria beautifulsoup para obtener las urls de la busqueda.
# Se ejecuta cuando el primer metodo falla
def recuperar_urls_beautifulsoup(q, n):
    bing = []
    consulta = q.replace(" ", "+")
    for i in range(1,2):
        print("https://www.bing.com/search?q=" + consulta + "&qs=n&cvid=A8821870F285403DAC8D935AD548A053&sp=3&first={0}".format(i*10))
        sauce = urllib2.urlopen(
            "https://www.bing.com/search?q=" + consulta + "&qs=n&form=QBLH&sp=-1&pq="+consulta+"&sc=2-0&sk=&cvid=105FD159528E4D039AEB0EA503BE825E&first={0}".format(i*10)).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')

        divs = soup.findAll("li", {"class": "b_algo"})
        for unDivs in divs:
            bing.append(unDivs.find('a').get('href'))
    return bing

#q=machine+learning&qs=AS&pq=machine+&sc=8-8&cvid=2ADFF9FFD60A4198A887E866FE7B8802&sp=1&first=50&FORM=PERE3