#----------Importaciones/Referencias-------------

from django.urls import path
from .views import UsuarioList

#------------------Codigo------------------------

urlpatterns = [
    path('usuario/', UsuarioList.as_view(), name='usuario_list'),
]
