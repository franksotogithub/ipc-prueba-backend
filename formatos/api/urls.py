from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import MovMercadoCabViewSet,MovMercadoDetViewSet

app_name = 'formatos_api'

router = DefaultRouter()
router.register(r'mov-mercado-cab',MovMercadoCabViewSet )
router.register(r'mov-mercado-det',MovMercadoDetViewSet )

urlpatterns = [

]

urlpatterns += router.urls