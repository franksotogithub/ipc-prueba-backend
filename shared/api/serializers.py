from rest_framework import serializers
from ..models import  DirectorioIPC, Producto, Investigador
from rest_framework.fields import ChoiceField

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class DirectorioIPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorioIPC
        fields = '__all__'

class InvestigadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investigador
        fields = '__all__'