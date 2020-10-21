#----------Importaciones/Referencias-------------

from django.db import models


#------------------Codigo------------------------

# Crear todos los modelos aqui.

class TipoUsuario(models.Model):
    tipoUsuarioId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=300)

    def __str__(self):
        return '{0}'.format(self.nombre)

class Usuario(models.Model):
    usuarioId = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=250)
    apellidoPaterno = models.CharField('ApellidoPaterno', max_length=250)
    apellidoMaterno = models.CharField('ApellidoMaterno', max_length=250) 
    fechaNacimiento = models.DateField('FechaNacimiento')
    email = models.EmailField('Email',max_length=255, unique=True)
    password = models.CharField('Password', max_length=500)
    activo = models.BooleanField('Activo',default=True)
    tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.nombre, self.apellidoPaterno)