#----------Importaciones/Referencias-------------

from django.contrib import admin

#from .models import TipoUsuario
from .models import Usuario
from .models import RecoverPasswordLog
from .models import Mastografia
#------------------Codigo------------------------

# Register your models here.

#admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(RecoverPasswordLog)
admin.site.register(Mastografia)