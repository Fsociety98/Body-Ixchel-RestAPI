# ----------./ Importaciones/Referencias /.-------------

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# ------------------./ Codigo /.------------------------

# Crear todos los modelos aqui.

# -----------------------Usuario--------------------------------


class UsuarioManager(BaseUserManager):

    def create_user(self, nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, email, password=None):

        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        usuario = self.model(nombre=nombre, apellidoPaterno=apellidoPaterno,
                             apellidoMaterno=apellidoMaterno, fechaNacimiento=fechaNacimiento, email=email)

        usuario.set_password(password)
        usuario.save(using=self.db)

        return usuario
    
    def create_superuser(self, nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, email, password):

        usuario = self.create_user(nombre, apellidoPaterno, apellidoMaterno, fechaNacimiento, email, password)

        usuario.is_superuser = True
        usuario.is_staff = True

        usuario.save(using=self.db)

        return usuario


class Usuario(AbstractBaseUser, PermissionsMixin):

    # Campos de la tabla.

    usuarioId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=250)
    apellidoPaterno = models.CharField('ApellidoPaterno', max_length=250)
    apellidoMaterno = models.CharField('ApellidoMaterno', max_length=250) 
    fechaNacimiento = models.DateField('FechaNacimiento')
    email = models.EmailField('Email',max_length=255, unique=True)
    password = models.CharField('Password', max_length=500)
    is_active = models.BooleanField('Activo',default=True)
    is_staff = models.BooleanField('Soporte', default=False)

    # Asignaciones.

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento']

    # Metodos.

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellidoPaterno)

# -----------------------Usuario--------------------------------
