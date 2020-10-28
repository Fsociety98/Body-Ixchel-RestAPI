#----------Importaciones/Referencias-------------
from django.contrib.auth import password_validation, authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import Usuario
from rest_framework.validators import UniqueValidator
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
            'is_active',
            'is_staff',
        )

class UsuarioLoginSerializer(serializers.Serializer):

    #Campos a requerir.
    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, max_length=64)

    #Validcion de datos.

    def validate(self, data):
        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        usuario = authenticate(username=data['email'], password=data['password'])

        if not usuario:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token

        self.context['usuario'] = usuario
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['usuario'])
        return self.context['usuario'], token.key


class UsuarioRegistroSerializer(serializers.Serializer):

    nombre = serializers.CharField(min_length=2, max_length=250)
    apellidoPaterno = serializers.CharField(min_length=2, max_length=250)
    apellidoMaterno = serializers.CharField(min_length=2, max_length=250)
    fechaNacimiento = serializers.DateField()

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )

    password = serializers.CharField(min_length=4, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        password_validation.validate_password(passwd)

        return data

    def create(self, data):
        data.pop('password_confirmation')
        usuario = Usuario.objects.create_user(**data)

        return usuario
