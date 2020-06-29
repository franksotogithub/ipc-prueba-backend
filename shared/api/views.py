from django.shortcuts import render
from datetime import datetime
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DirectorioIPCSerializer,ProductoSerializer ,InvestigadorSerializer
from ..models import DirectorioIPC , Producto, Investigador

class DirectorioIPCViewSet(ModelViewSet):
    queryset = DirectorioIPC.objects.all()
    serializer_class = DirectorioIPCSerializer

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class InvestigadorViewSet(ModelViewSet):
    queryset = Investigador.objects.all()
    serializer_class = InvestigadorSerializer