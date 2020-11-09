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
            
            """
            data = {
                'errors': 'Las credenciales no son válidas'
            }
            raise serializers.ValidationError(data)
            """
            
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token

        self.context['usuario'] = usuario
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['usuario'])
        return self.context['usuario'], token.key


class UsuarioRegistroSerializer(serializers.Serializer):

    nombre = serializers.CharField(min_length=2, max_length=250, error_messages={'blank':'El campo Nombre no puede estar vacío.'})
    apellidoPaterno = serializers.CharField(min_length=2, max_length=250, error_messages={'blank':'El campo Apellido Paterno no puede estar vacío.'})
    apellidoMaterno = serializers.CharField(min_length=2, max_length=250, error_messages={'blank':'El campo Apellido Materno no puede estar vacío.'})
    fechaNacimiento = serializers.DateField()

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=Usuario.objects.all())],
        error_messages={'blank':'El campo Email no puede estar vacío.'}
    )

    password = serializers.CharField(min_length=4, max_length=64, error_messages={'blank':'El campo Contraseña no puede estar vacío.'})
    password_confirmation = serializers.CharField(min_length=4, max_length=64, error_messages={'blank':'El campo Confirmar Contraseña no puede estar vacío.'})

    def validate(self, data):

        #errors_list = []

        passwd = data['password']
        passwd_conf = data['password_confirmation']

        if passwd != passwd_conf:
            data = {
                'errors': 'Las contraseñas no coinciden.'
            }
            raise serializers.ValidationError(data)

        password_validation.validate_password(passwd)
        
        return data

    def create(self, data):
        data.pop('password_confirmation')
        usuario = Usuario.objects.create_user(**data)

        return usuario
    """
    def update(self, instance, validate_data):
        instance.nombre = validate_data.get('nombre', instance.nombre)
        instance.apellidoPaterno = validate_data.get('apellidoPaterno', instance.apellidoPaterno)
        instance.apellidoMaterno = validate_data.get('apellidoMaterno', instance.apellidoMaterno)
        instance.fechaNacimiento = validate_data.get('fechaNacimiento', instance.fechaNacimiento)
        instance.email = validate_data.get('email', instance.email)
        return instance
    """

class UsuarioModificarDatosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'usuarioId',
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'fechaNacimiento',
            'email',
        )

class UsuarioInactivoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = (
            'usuarioId',
            'is_active',
        )

class UsuarioCambioPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password_old = serializers.CharField(min_length=4, max_length=64)
    new_password = serializers.CharField(min_length=4, max_length=64)
    new_password_confirmation = serializers.CharField(min_length=8, max_length=64)

def validate(self, data):
        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        usuario = authenticate(username=data['email'], password=data['password_old'])

        if not usuario:
            raise serializers.ValidationError('Las credenciales no son válidas')

        return True