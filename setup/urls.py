from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# --- IMPORTAÇÕES DO SWAGGER ---
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Escola API",
      default_version='v1',
      description="API local para gerenciamento de alunos, cursos e matrículas",
      terms_of_service="#",
      contact=openapi.Contact(email="seuemail@exemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
# ------------------------------

# Importações da V1 e V2 (MANTENHA O QUE JÁ ESTAVA AQUI)
from escola.api.v1.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudante, ListaEstudantesMatriculados
from escola.api.v2.views import EstudanteViewSetV2

router_v1 = routers.DefaultRouter()
router_v1.register('estudantes', EstudanteViewSet, basename='Estudantes')
router_v1.register('cursos', CursoViewSet, basename='Cursos')
router_v1.register('matriculas', MatriculaViewSet, basename='Matriculas')

router_v2 = routers.DefaultRouter()
router_v2.register('estudantes', EstudanteViewSetV2, basename='EstudantesV2')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router_v1.urls)),
    path('v1/estudantes/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('v1/cursos/<int:pk>/matriculas/', ListaEstudantesMatriculados.as_view()),
    path('v2/', include(router_v2.urls)),
    
    # --- ROTAS DO SWAGGER ---
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]