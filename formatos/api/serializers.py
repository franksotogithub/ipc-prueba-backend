from rest_framework import serializers
from ..models import  MovMercadoCab , MovMercadoDet
#from ..models import Usuario, ComprobanteCab ,ComprobanteDet ,\
#    EstadoDocumento,ResumenCab,ResumenDet,Cliente

class MovMercadoDetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovMercadoDet
        fields = '__all__'


class MovMercadoCabSerializer(serializers.ModelSerializer):
    detalles = MovMercadoDetSerializer(many=True)
    class Meta:
        model = MovMercadoCab
        fields = ('anio','mes','n_semana','n_dia','hora_ini','hora_fin','inv','mercado','detalles')

    def create(self, validated_data):
        detalles_data = validated_data.pop('detalles')
        movMercadoCab = MovMercadoCab.objects.create(**validated_data)
        for detalle_data in detalles_data:
            MovMercadoDet.objects.create(movMercadoCab,detalle_data)
        return movMercadoCab

