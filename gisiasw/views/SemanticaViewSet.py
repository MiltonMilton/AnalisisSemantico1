from gisiasw.serializers.URLSerializer import URLSerializer
from gisiasw.models.models import URL
from rest_framework import viewsets
from rest_framework.response import Response
from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager

class SemanticaViewSet(viewsets.ModelViewSet):


    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):

        #wsrequest = URLSerializer(data=request.data)
        #print(wsrequest)
        reponse = {}
        #if(wsrequest.is_valid()):
        #    response = wsrequest.data

        analizador = AnalisisSemanticoManager()
        data = request.data
        data, edges = analizador.analizar(data)
        response = Response({"status": "ok", "nodes": data, "edges": edges})
        response["Access-Control-Allow-Origin"] = "*"

        return response
