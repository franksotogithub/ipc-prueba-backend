from django.db import models
from shared.models import DirectorioIPC ,  Investigador , Producto
# Create your models here.
class MovMercadoCab(models.Model):
    id = models.AutoField( primary_key=True, )
    anio = models.CharField(max_length=4, blank=True, null=True)
    mes = models.CharField(max_length=2, blank=True, null=True)
    n_semana = models.CharField(max_length=1, blank=True, null=True)
    n_dia = models.CharField(max_length=1, blank=True, null=True)
    hora_ini = models.CharField(max_length=10, blank=True, null=True)
    hora_fin = models.CharField(max_length=10, blank=True, null=True)
    inv = models.ForeignKey( Investigador, blank=True, null=True,on_delete=models.DO_NOTHING)
    mercado = models.ForeignKey(DirectorioIPC, blank=True, null=True,on_delete=models.DO_NOTHING)


class MovMercadoDet(models.Model):
    CE_CHOICES = [
        (1,"Abundancia"),
        (2, "Normal"),
        (3, "Escacez"),
        (4, "Escaces total")
    ]

    CC_CHOICES = [
        (1, "Nominal"),
        (2, "Compra"),

    ]
    id = models.AutoField(primary_key=True)
    mov_mercado_cab = models.ForeignKey(MovMercadoCab,related_name='detalles',null=True,blank=True,on_delete=models.DO_NOTHING)
    producto =  models.ForeignKey(Producto, blank=True, null=True, on_delete=models.DO_NOTHING)
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    peso = models.DecimalField(max_digits=5, decimal_places=0, blank=True, null=True)
    ce = models.CharField(max_length=1, blank=True, null=True,choices=CE_CHOICES)
    cc = models.CharField(max_length=1, blank=True, null=True,choices=CC_CHOICES)


