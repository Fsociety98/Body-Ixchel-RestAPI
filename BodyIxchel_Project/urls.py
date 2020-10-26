"""BodyIxchel_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
#----------Importaciones/Referencias-------------

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from BodyIxchel_API.views import Login, Logout

#------------------Codigo------------------------

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(('BodyIxchel_API.urls','api'))),
    path('api_generate_token/',views.obtain_auth_token),
    path('login/',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
]
"""
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    path('', include(('BodyIxchel_API.urls', 'usuario'), namespace='usuario')),

]