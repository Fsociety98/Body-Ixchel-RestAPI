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

# -----------------------Recuperar Contraseña--------------------------------

class RecoverPasswordLog(models.Model):
    recoverPasswordLogId = models.AutoField(primary_key=True)
    codigo = models.CharField('Codigo', max_length=250)
    fechaSolicitud = models.DateField('FechaSolicitud')
    validado = models.BooleanField('Validado',default=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.codigo)


# -----------------------Recuperar Contraseña--------------------------------

# -----------------------Mastografia--------------------------------

"""
class Mastografia(models.Model):
    mastografiaId = models.AutoField(primary_key=True)
    rutaImagenOriginal = models.CharField('RutaImagenOriginal', max_length=750)
    rutaImagenResultado = models.CharField('RutaImagenResultado', max_length=750)
    fechaEscaneo = models.DateField('FechaEscaneo')
    anomaliasEncontradas = models.IntegerField('AnomaliasEncontradas', default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.mastografiaId)

"""

class Mastografia(models.Model):
    mastografiaId = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to = 'mastografias', default = 'mastografias/static/images/no-img.jpg')
    fechaEscaneo = models.DateField('FechaEscaneo')
    check = models.BooleanField('Check',default=False)
    anomaliasEncontradas = models.IntegerField('AnomaliasEncontradas', default=0)
    idMastografiaOriginal = models.IntegerField('IdMastografiaOriginal', default=0)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.mastografiaId)


# -----------------------Mastografia--------------------------------