from django.shortcuts import render
from datetime import datetime

from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import MovMercadoCabSerializer , MovMercadoDetSerializer
from django.views.generic import TemplateView
from django.db.models import Count, Max, Case, When, Sum , F
from django.shortcuts import get_object_or_404 ,Http404
import os
from django.conf import settings
from django.http import HttpResponse

from  ..models import MovMercadoDet ,MovMercadoCab

class MovMercadoCabViewSet(ModelViewSet):
    queryset = MovMercadoCab.objects.all()
    serializer_class = MovMercadoCabSerializer


class MovMercadoDetViewSet(ModelViewSet):
    queryset = MovMercadoDet.objects.all()
    serializer_class = MovMercadoDetSerializer