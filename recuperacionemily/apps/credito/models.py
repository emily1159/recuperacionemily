from django.db import models

# Create your models here.
class credito(models.Model):
    acumulado = models.IntegerField("Acumulado")
    valor = models.IntegerField("Valor")