from django.db import models

class Ficha(models.Model):
    nro_id = models.AutoField(primary_key=True)
    nro_sigla_cicpse = models.IntegerField()
    nombre_coleccion = models.CharField(max_length=200)

    # Campos opcionales
    sigla_renicoa = models.CharField(max_length=100, blank=True, null=True)
    otros_nro_registro = models.CharField(max_length=100, blank=True, null=True)
    nombre_descriptivo = models.CharField(max_length=200, blank=True, null=True)
    tipo_material = models.CharField(max_length=100, blank=True, null=True)
    anio_coleccion = models.CharField(max_length=4, blank=True, null=True)
    forma_ingreso = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=200, blank=True, null=True)
    otros_datos = models.TextField(blank=True, null=True)
