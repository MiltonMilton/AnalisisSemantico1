"""gisiasw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from gisiasw.views import AnalizadorViewSet2
from gisiasw.views.SemanticaViewSet import SemanticaViewSet
from gisiasw.views.AnalizadorViewSet import AnalizadorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'analizar', AnalizadorViewSet)

urlpatterns = router.urls
#urlpatterns = [
 #   url(r'^', include(router.urls))
    #url(r'^admin/', admin.site.urls),
    #url(r'^api-auth/', include('rest_framework.urls'))
    #url(r'^analizar/(?P<process_id>[\w-]+)/$', SemanticaController.analizar)
#]

#router.register(r'search/html/$', AnalizadorController.buscarHTML)
#router.register(r'search/doc/$', AnalizadorController.buscarDoc)
#router.register(r'search/pdf/$', AnalizadorController.buscarPDF)
