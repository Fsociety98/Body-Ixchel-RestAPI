README.MD

Body-Ixchel API

#Contenido

Este proyecto esta en github en dos ramas : Master, Deploy

#Demo
URL del proyecto en servidor :


#Instalacion

PASO 1
*Ejecutar el comando : pip install -r requirements.txt

PASO 2 
*"En caso de proyecto nuevo"

ejecutar : 
django-admin startproject NAMEOFPROJECT
python manage.py startapp NAMEOFPROJECT

#Ejecucion

*Para la creacion/actualizacion de modelos.
python manage.py makemigrations
python manage.py migrate

*Para crear un superusuario:
python manage.py createsuperuser

*Base de datos:
-En caso de no funcionar, instalar el paquete PyMySQL
pip install PyMySQL

PARA CORRER EL PROYECTO : python manage.py runserver 

#Notas
*En requirements.txt se indicaran los paquetes basicos a instalar para la ejecucion del proyecto.
*El comando "makemigrations" generara un archvio en la carpeta "migrations" con la info de la tabla a crear.
*El comando "migrate" cargara todos los modelos nuevos o actualizaciones a la base de datos.