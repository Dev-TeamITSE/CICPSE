from django.db import models

class Ficha(models.Model):
    nro_id = models.IntegerField(unique=True)
    nro_sigla_cicpse = models.IntegerField()
    sigla_renicoa = models.CharField(max_length=100, blank=True, null=True)
    otros_nro_registro = models.CharField(max_length=100, blank=True, null=True)
    nombre_coleccion = models.CharField(max_length=200)
    nombre_descriptivo = models.CharField(max_length=200, blank=True, null=True)
    tipo_material = models.CharField(max_length=100)
    anio_coleccion = models.CharField(max_length=4, blank=True, null=True)
    forma_ingreso = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200)
    otros_datos = models.TextField(blank=True, null=True)

    # Datos de procedencia
    pais = models.CharField(max_length=100, blank=True, null=True)
    provincia_region = models.CharField(max_length=100, blank=True, null=True)
    departamento = models.CharField(max_length=100, blank=True, null=True)
    localidad = models.CharField(max_length=100, blank=True, null=True)
    sitio_arqueologico = models.CharField(max_length=200, blank=True, null=True)
    datos_contextuales = models.TextField(blank=True, null=True)

    # Descripción del objeto
    altura_largo = models.FloatField(blank=True, null=True)
    ancho_diametro_maximo = models.FloatField(blank=True, null=True)
    espesor = models.FloatField(blank=True, null=True)
    otras_alturas = models.FloatField(blank=True, null=True)
    diametro_minimo = models.FloatField(blank=True, null=True)
    otras_medidas = models.TextField(blank=True, null=True)
    forma = models.CharField(max_length=200, blank=True, null=True)
    tecnica = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    adscripcion_cultural_temporal = models.CharField(max_length=200, blank=True, null=True)

    # Estado de conservación
    estado_conservacion = models.CharField(max_length=50, choices=[
        ('malo', 'Malo'),
        ('regular', 'Regular'),
        ('bueno', 'Bueno'),
        ('muy bueno', 'Muy Bueno'),
    ])
    estado_estructural = models.CharField(max_length=50, choices=[
        ('entero', 'Entero'),
        ('fragmentado', 'Fragmentado'),
        ('completo', 'Completo'),
        ('incompleto', 'Incompleto'),
    ])
    
    estado_superficie = models.CharField(max_length=50, choices=[
        ('sin_deterioro', 'Sin deterioro'),
        ('suciedad_superficial', 'Suciedad Superficial'),
        ('depositos_foraneos', 'Depósitos Foráneos'),
    ])
    
    intervenciones = models.TextField(blank=True, null=True)
    observaciones = models.TextField(blank=True, null=True)
    
    fecha_registro = models.DateField()
    nombre_apellido = models.CharField(max_length=200)
    dni = models.IntegerField()
    designacion = models.CharField(max_length=100)
    contacto = models.CharField(max_length=50)

    def __str__(self):
        return f"Ficha {self.nro_id}"
