from django.db import models

class Page(models.Model):
    content = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table='page'