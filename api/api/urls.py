from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet, FuncionarioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

router = routers.DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
