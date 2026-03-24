from rest_framework import serializers
from escola.models import Estudante

class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'cpf'] # RG e Data Ocultos