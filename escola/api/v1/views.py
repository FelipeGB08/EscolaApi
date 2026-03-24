from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from escola.models import Estudante, Curso, Matricula
from escola.api.v1.serializers import (
    EstudanteSerializer, CursoSerializer, MatriculaSerializer,
    ListaMatriculasEstudanteSerializer, ListaEstudantesMatriculadosSerializer
)

class EstudanteViewSet(viewsets.ModelViewSet):
    """Exibe todos os estudantes da V1"""
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

class CursoViewSet(viewsets.ModelViewSet):
    """Exibe todos os cursos da V1"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['codigo_curso']
    search_fields = ['codigo_curso', 'descricao']

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibe todas as matrículas da V1"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasEstudante(generics.ListAPIView):
    """Lista as matrículas de um estudante específico na V1"""
    serializer_class = ListaMatriculasEstudanteSerializer
    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])

class ListaEstudantesMatriculados(generics.ListAPIView):
    """Lista os estudantes matriculados em um curso específico na V1"""
    serializer_class = ListaEstudantesMatriculadosSerializer
    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])