from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from escola.models import Estudante
from escola.api.v2.serializers import EstudanteSerializerV2

class EstudanteViewSetV2(viewsets.ModelViewSet):
    """Exibe todos os estudantes da V2"""
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializerV2
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']