from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from BodyIxchel_API import views

router = DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls))
]