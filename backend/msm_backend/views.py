from rest_framework import viewsets
from rest_framework.response import Response
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

    def create(self, request, *args, **kwargs):
        serializer = CreateMonsterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        monster = serializer.save()
        serializer = MonsterSerializer(monster)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CreateMonsterSerializer(
            instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        monster = serializer.save()
        serializer = MonsterSerializer(monster)
        return Response(serializer.data)
