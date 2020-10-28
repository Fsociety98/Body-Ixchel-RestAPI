from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from BodyIxchel_API import views

router = DefaultRouter()
router.register(r'authentication', views.AuthenticationViewSet, basename='authentication')
#router.register(r'users', views.UsuarioViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls)),
    #path('logout/', views.Logout.as_view())
   path('users/all', views.getUsers, name='user_all'),
   path('users/detail/<int:user_id>', views.getUser, name='user_detail'),
]