# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
# Serializers
from BodyIxchel_API.serializers import UsuarioLoginSerializer, UsuarioSerializer, UsuarioRegistroSerializer

# Models
from BodyIxchel_API.models import Usuario

#------------ Authentication ---------------

class AuthenticationViewSet(viewsets.GenericViewSet):

    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post.

    #/api/authentication/login/
    #BODY: {"email": "", "password": ""}

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
    
    #/api/authentication/create_account/
    #BODY : {"nombre": "", "apellidoPaterno": "", "apellidoMaterno": "", "fechaNacimiento": "YYYY-MM-DD",
    #"email": "", "password": "", "password_confirmation" : "", "is_active": false, "is_staff": false }

    @action(detail=False, methods=['post'])
    def create_account(self, request):
        serializer = UsuarioRegistroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        usuario = serializer.save()
        data = UsuarioSerializer(usuario).data
        return Response(data, status=status.HTTP_201_CREATED)

    #/api/authentication/logout/
    #HEADERS: [KEY : Authorization, VALUE : Token {token}]

    @action(detail=False, methods=['get'])
    def logout(self, request, format=None):
        queryset = self.get_queryset()
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


#------------ Authentication ---------------

#-- APARTIR DE AQUI TODOS :: HEADERS: [KEY : Authorization, VALUE : Token {token}]

#------------ Usuario ---------------

#/api/users/all
@api_view(["GET"])
@permission_classes([IsAuthenticated])  
def getUsers(request):
    queryset = Usuario.objects.filter(is_active=True)
    serializer = UsuarioSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#/api/users/detail/{user_id}
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getUser(request, user_id):

    queryset = Usuario.objects.filter(is_active=True, usuarioId=user_id)
    validator = queryset.exists()

    if validator == True :
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else :
        return Response({'error': 'Usuario no encontrado.'}, status=status.HTTP_404_NOT_FOUND)

#@api_view(["PUT"])
#@permission_classes([IsAuthenticated])
#def updateUser(request, user_id):








"""
class UsuarioViewSet(viewsets.GenericViewSet):
    
    queryset = Usuario.objects.filter(is_active=True)
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated, )

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = self.get_queryset()
        serializer = UsuarioSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def detail(self, request, pk=None):
        print(pk)
        #queryset = self.get_queryset()

        #usuario = get_object_or_404(queryset, pk=pk)
        #serializer = UsuarioSerializer(usuario)



        #serializer = UsuarioSerializer(queryset, many=True)
        #return Response(serializer.data)
        return Response({'ss':'w'})
"""
#------------ Usuario ---------------