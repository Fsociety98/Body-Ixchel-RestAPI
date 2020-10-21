#----------Importaciones/Referencias-------------

from rest_framework import serializers
from .models import Usuario

#------------------Codigo------------------------


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'usuarioId',
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'fechaNacimiento',
            'email',
            'password',
            'activo',
            'tipoUsuario',
        )


    #name = serializers.CharField(max_length=10)