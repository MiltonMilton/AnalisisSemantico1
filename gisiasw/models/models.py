from django.db import models

class Page(models.Model):
    content = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table='page'

class URL(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    valoracion = models.DecimalField()
    votos = models.IntegerField()

    class Meta:
        db_table='url_processed'
