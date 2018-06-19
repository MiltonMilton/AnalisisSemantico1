from gisiasw.serializers.URLSerializer import URLSerializer
from gisiasw.models.models import URL
from rest_framework import viewsets
from rest_framework.response import Response
from gisiasw.managers.Analisis import Analisis

class AnalizadorViewSet(viewsets.ModelViewSet):


    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):

        #wsrequest = URLSerializer(data=request.data)
        #print(wsrequest)
        reponse = {}
        #if(wsrequest.is_valid()):
        #    response = wsrequest.data

        analizador = Analisis()
        data = request.data
        resultado = analizador.armarMatrizdeSimilitudes(data.get("claves"), data.get("metodo"), data.get("urls"))
        response = Response({"status": "ok", "matrices":resultado.get("matrices"), "claves": resultado.get("claves")})
        response["Access-Control-Allow-Origin"] = "*"

        return response
