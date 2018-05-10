from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from gisiasw.serializers.URLSerializer import URLSerializer
from gisiasw.models.models import URL
from rest_framework import viewsets
from rest_framework.decorators import  list_route
from rest_framework.response import Response

class SemanticaController(viewsets.ModelViewSet):

    queryset = URL.objects.all()
    serializer_class = URLSerializer

    @csrf_exempt
    def create(self, request, *args, **kwargs):
        print(request.data)
        #wsrequest = URLSerializer(data=request.data)
        reponse = {}
        #if(wsrequest.is_valid()):
        #    response = wsrequest.data

        return Response(data=request.data)
