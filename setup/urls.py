from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views_frontend import index
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Documentação
schema_view = get_schema_view(
   openapi.Info(title="Escola API", default_version='v1'),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Roteadores
from escola.api.v1.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet
from escola.api.v2.views import EstudanteViewSetV2

router_v1 = routers.DefaultRouter()
router_v1.register('estudantes', EstudanteViewSet, basename='EstudantesV1')
router_v1.register('cursos', CursoViewSet, basename='CursosV1')
router_v1.register('matriculas', MatriculaViewSet, basename='MatriculasV1')

router_v2 = routers.DefaultRouter()
router_v2.register('estudantes', EstudanteViewSetV2, basename='EstudantesV2')

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('v1/', include(router_v1.urls)),
    path('v2/', include(router_v2.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]