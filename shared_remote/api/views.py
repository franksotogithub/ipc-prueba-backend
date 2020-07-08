from django.shortcuts import render
from datetime import datetime
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import SipDirectorioIpcSerializer,SipInvestigadorSerializer\

    #,SipMVariedadSerializer
from ..models import SipDirectorioIpc,SipInvestigador\
    #,SipMVariedad
#
class SipDirectorioIpcViewSet(ModelViewSet):
    queryset = SipDirectorioIpc.objects.all()
    serializer_class = SipDirectorioIpcSerializer

    @action(detail=False)
    def get_directorio(self, request):
        print(request.query_params)
        pass

#
class SipInvestigadorViewSet(ModelViewSet):
    queryset = SipInvestigador.objects.all()
    serializer_class = SipInvestigadorSerializer



#class SipMVariedadViewSet(ModelViewSet):
#    queryset = SipMVariedad.objects.all()
#    serializer_class = SipMVariedadSerializer