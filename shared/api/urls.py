from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet,DirectorioIPCViewSet , InvestigadorViewSet




app_name = 'formatos_api'

router = DefaultRouter()
router.register(r'producto',ProductoViewSet )
router.register(r'directorio',DirectorioIPCViewSet )
router.register(r'investigador',InvestigadorViewSet )
urlpatterns = [
]

urlpatterns += router.urls