from rest_framework.decorators import api_view
from rest_framework.response import Response
from gisiasw.scrapper.Scrapper import Scrapper

@api_view(['GET'])
def buscarHTML(request):
    """
       Busca dada una URL el contenido de una pagina, pdf o documento de texto y devuelve el contendio del mismo
    """

    url = str(request.GET.get('url'))
    scrapper=Scrapper()

    return Response({
        "status": "OK",
        "content":scrapper.buscarHTML("", url)
    })

@api_view(['GET'])
def buscarPDF(request):
    """
       Busca dada una URL el contenido de una pagina, pdf o documento de texto y devuelve el contendio del mismo
    """

    url = str(request.GET.get('url'))
    scrapper=Scrapper()

    return Response({
        "status": "OK",
        "content":scrapper.buscarPDF("", url)
    })

@api_view(['GET'])
def buscarDoc(request):
    """
       Busca dada una URL el contenido de una pagina, pdf o documento de texto y devuelve el contendio del mismo
    """

    url = str(request.GET.get('url'))
    scrapper=Scrapper()

    return Response({
        "status": "OK",
        "content":scrapper.buscarDoc("", url)
    })
