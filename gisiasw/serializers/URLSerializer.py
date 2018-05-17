from rest_framework import serializers
from gisiasw.models.models import URL

class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ('name','url','valoracion','votos')