import subprocess
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from gisiasw.serializers.URLSerializer import URLSerializer
from gisiasw.models.models import URL
from rest_framework import viewsets
from rest_framework.decorators import  list_route
from rest_framework.response import Response
from gisiasw.managers.AnalisisSemanticoManager import AnalisisSemanticoManager


class SemanticaViewSet(viewsets.ModelViewSet):


    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def create(self, request, *args, **kwargs):

        analizador = AnalisisSemanticoManager()
        data = request.data
        return Response({"status":"ok", "data": analizador.analizar(data)})
