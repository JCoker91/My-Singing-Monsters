from rest_framework import viewsets
from .serializers import MonsterSerializer
from .models import Monster

class MonsterViewSet(viewsets.ModelViewSet):
    queryset = Monster.objects.all()
    serializer_class = MonsterSerializer