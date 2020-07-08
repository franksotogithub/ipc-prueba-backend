from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import SipDirectorioIpcViewSet,SipInvestigadorViewSet\
    #,SipMVariedadViewSet




app_name = 'shared_remote_api'

router = DefaultRouter()
#router.register(r'producto',SipMVariedadViewSet )
router.register(r'directorio',SipDirectorioIpcViewSet )
router.register(r'investigador',SipInvestigadorViewSet )
urlpatterns = [
]

urlpatterns += router.urls