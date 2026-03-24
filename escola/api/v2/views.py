from rest_framework import viewsets
from escola.models import Estudante
from escola.api.v2.serializers import EstudanteSerializerV2

class EstudanteViewSetV2(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializerV2