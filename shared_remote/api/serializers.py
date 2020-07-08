from rest_framework import serializers
from ..models import  SipDirectorioIpc,SipInvestigador\
    #,SipMVariedad
#from rest_framework.fields import ChoiceField
#
class SipDirectorioIpcSerializer(serializers.ModelSerializer):
    class Meta:
        model = SipDirectorioIpc
        fields = '__all__'
#
class SipInvestigadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SipInvestigador
        fields = '__all__'
#
#class SipMVariedadSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = SipMVariedad
#        fields = '__all__'