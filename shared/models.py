from django.db import models

# Create your models here.
class DirectorioIPC(models.Model):
    id = models.CharField(primary_key=True,max_length=8)
    ruc = models.CharField(max_length=11, blank=True, null=True)
    razon_social = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.razon_social


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Investigador(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return "{} {}".format(self.codigo,self.nombre)