from rest_framework import viewsets
from .serializers import MonsterSerializer, CreateMonsterSerializer
from .models import Monster


class MonsterViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch',
                         'put', 'delete', 'head', 'options']

    queryset = Monster.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return CreateMonsterSerializer
        return MonsterSerializer
