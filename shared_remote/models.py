from django.db import models

# Create your models here.
class SipDirectorioIpc(models.Model):
    anio_base = models.CharField(db_column='ANIO_BASE', max_length=4)  # Field name made lowercase.
    ciu_codigo = models.CharField(db_column='CIU_CODIGO', max_length=2)  # Field name made lowercase.
    cod_info = models.CharField( db_column='COD_INFO', max_length=8)  # Field name made lowercase.
    #cod_info = models.ForeignKey('SipDirectorio', models.DO_NOTHING, db_column='COD_INFO')  # Field name made lowercase.
    cod_info_ipc = models.CharField(db_column='COD_INFO_IPC', max_length=8)  # Field name made lowercase.
    id_directorio_ipc = models.AutoField(db_column='ID_DIRECTORIO_IPC', primary_key=True)  # Field name made lowercase.
    cod_info2 = models.CharField(db_column='COD_INFO2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='REFERENCIA', max_length=150, blank=True, null=True)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=35, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    manzana = models.CharField(db_column='MANZANA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    frente = models.CharField(db_column='FRENTE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    fecha_ingreso = models.DateTimeField(db_column='FECHA_INGRESO', blank=True, null=True)  # Field name made lowercase.
    fecha_baja = models.DateTimeField(db_column='FECHA_BAJA', blank=True, null=True)  # Field name made lowercase.
    situacion = models.CharField(db_column='SITUACION', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cir_codigo = models.CharField(db_column='CIR_CODIGO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    cir_orden = models.CharField(db_column='CIR_ORDEN', max_length=3, blank=True, null=True)  # Field name made lowercase.
    giro_codigo = models.CharField(db_column='GIRO_CODIGO', max_length=3, blank=True, null=True)  # Field name made lowercase.
    sector = models.CharField(db_column='SECTOR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    division = models.CharField(db_column='DIVISION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    clase = models.CharField(db_column='CLASE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    #dpto_codigo = models.ForeignKey('SipDistrito', models.DO_NOTHING, db_column='DPTO_CODIGO', blank=True, null=True)  # Field name made lowercase.
    #prov_codigo = models.ForeignKey('SipDistrito', models.DO_NOTHING, db_column='PROV_CODIGO', blank=True, null=True)  # Field name made lowercase.
    #dist_codigo = models.ForeignKey('SipDistrito', models.DO_NOTHING, db_column='DIST_CODIGO', blank=True, null=True)  # Field name made lowercase.
    nro_comerciantes = models.IntegerField(db_column='NRO_COMERCIANTES', blank=True, null=True)  # Field name made lowercase.
    tipo_informante = models.CharField(db_column='TIPO_INFORMANTE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fec_estado = models.DateTimeField(db_column='FEC_ESTADO', blank=True, null=True)  # Field name made lowercase.
    dia_semana = models.CharField(db_column='DIA_SEMANA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ubigeo = models.CharField(db_column='UBIGEO', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nom_distrito = models.CharField(db_column='NOM_DISTRITO', max_length=80, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='DIRECCION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    nro = models.CharField(db_column='NRO', max_length=15, blank=True, null=True)  # Field name made lowercase.
    piso = models.CharField(db_column='PISO', max_length=8, blank=True, null=True)  # Field name made lowercase.
    interior = models.CharField(db_column='INTERIOR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    mzna = models.CharField(db_column='MZNA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lote = models.CharField(db_column='LOTE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    km = models.CharField(db_column='KM', max_length=8, blank=True, null=True)  # Field name made lowercase.
    block = models.CharField(db_column='BLOCK', max_length=8, blank=True, null=True)  # Field name made lowercase.
    #cod_categoria = models.ForeignKey('SipCategoria', models.DO_NOTHING, db_column='COD_CATEGORIA', blank=True, null=True)  # Field name made lowercase.
    cir_tipo = models.CharField(db_column='CIR_TIPO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cuadra = models.CharField(db_column='CUADRA', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIP_DIRECTORIO_IPC'
        unique_together = (('anio_base', 'ciu_codigo', 'cod_info', 'cod_info_ipc'),)


class SipInvestigador(models.Model):
    ciu_codigo = models.CharField( db_column='CIU_CODIGO', max_length=2)  # Field name made lowercase.
    #ciu_codigo = models.ForeignKey('SipCiudad', models.DO_NOTHING, db_column='CIU_CODIGO')  # Field name made lowercase.
    inv_codigo = models.CharField(db_column='INV_CODIGO', max_length=2, primary_key=True)  # Field name made lowercase.
    inv_nombre = models.CharField(db_column='INV_NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inv_estado = models.CharField(db_column='INV_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SIP_INVESTIGADOR'
        unique_together = (('ciu_codigo', 'inv_codigo'),)


#class SipMVariedad(models.Model):
#    anio_base = models.CharField( db_column='ANIO_BASE', max_length=4, blank=True, null=True)  # Field name made lowercase.
#    cod_division = models.CharField(  db_column='COD_DIVISION', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_grupo = models.CharField( db_column='COD_GRUPO', max_length=8, blank=True, null=True)  # Field name made lowercase.
#    cod_clase = models.CharField( db_column='COD_CLASE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_subclase = models.CharField( db_column='COD_SUBCLASE', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_rubro = models.CharField( db_column='COD_RUBRO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_producto = models.CharField( db_column='COD_PRODUCTO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_articulo = models.CharField( db_column='COD_ARTICULO', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    cod_variedad = models.CharField(db_column='COD_VARIEDAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    vari_nombre = models.CharField(db_column='VARI_NOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#    var_rptnombre = models.CharField(db_column='VAR_RPTNOMBRE', max_length=100, blank=True, null=True)  # Field name made lowercase.
#    producto_nombre = models.CharField(db_column='PRODUCTO_NOMBRE', max_length=250, blank=True, null=True)  # Field name made lowercase.
#    var_codigo_14 = models.CharField(db_column='VAR_CODIGO_14', max_length=14, blank=True, null=True)  # Field name made lowercase.
#    var_estado = models.CharField(db_column='VAR_ESTADO', max_length=1, blank=True, null=True)  # Field name made lowercase.
#    tipo_encu = models.CharField(db_column='TIPO_ENCU', max_length=2, blank=True, null=True)  # Field name made lowercase.
#    canasta = models.CharField(db_column='CANASTA', max_length=1, blank=True, null=True)  # Field name made lowercase.
#    fecha_reg = models.DateTimeField(db_column='FECHA_REG', blank=True, null=True)  # Field name made lowercase.
#    fecha_act = models.DateTimeField(db_column='FECHA_ACT', blank=True, null=True)  # Field name made lowercase.
#    fecha_eli = models.DateTimeField(db_column='FECHA_ELI', blank=True, null=True)  # Field name made lowercase.
#    usuario = models.CharField(db_column='USUARIO', max_length=30, blank=True, null=True)  # Field name made lowercase.
#    id_usuario = models.IntegerField(db_column='ID_USUARIO', blank=True, null=True)  # Field name made lowercase.
#    ciudad = models.CharField(db_column='CIUDAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
#
#    class Meta:
#        managed = False
#        db_table = 'SIP_M_VARIEDAD'
#        unique_together = (('anio_base', 'cod_division', 'cod_grupo', 'cod_clase', 'cod_subclase', 'cod_rubro', 'cod_producto', 'cod_articulo', 'cod_variedad'),)