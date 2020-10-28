# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Serializers
from BodyIxchel_API.serializers import UsuarioLoginSerializer, UsuarioSerializer, UsuarioRegistroSerializer

# Models
from BodyIxchel_API.models import Usuario

class UsuarioViewSet(viewsets.GenericViewSet):

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        serializer = UsuarioLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario, token = serializer.save()
        data = {
            'usuario': UsuarioSerializer(usuario).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def registro(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.save()
        data = UsuarioSerializer(usuario).data
        return Response(data, status=status.HTTP_201_CREATED)

    """
    @action(detail=False, methods=['get'])
    def lista(self, request):
        queryset = Usuario.objects.filter(is_active=True)
        serializer = UsuarioSerializer
        usuarios = serializer.save()
        data = UsuarioSerializer(usuarios).data
        return Response(data)
    """
