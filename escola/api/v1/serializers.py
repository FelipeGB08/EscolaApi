from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
from escola.validators import *

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

    def validate(self, dados):
        if cpf_invalido(dados.get('cpf', '')):
            raise serializers.ValidationError({'cpf': "O CPF deve ter 11 dígitos."})
        if rg_invalido(dados.get('rg', '')):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 dígitos."})
        if nome_invalido(dados.get('nome', '')):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo."})
        return dados

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaEstudantesMatriculadosSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']