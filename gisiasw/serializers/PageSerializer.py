from rest_framework import serializers
from gisiasw.models.models import Page

class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('url', 'name', 'content')