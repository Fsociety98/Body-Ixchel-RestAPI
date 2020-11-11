from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from BodyIxchel_API import views

router = DefaultRouter()
router.register(r'authentication', views.AuthenticationViewSet, basename='authentication')



urlpatterns = [
    path('', include(router.urls)),
    #path('logout/', views.Logout.as_view())
   path(r'users/all', views.getUsers, name='user_all'),
   path(r'users/detail/<int:user_id>', views.getUser, name='user_detail'),
   path(r'users/update/<int:user_id>', views.updateUser, name='user_update'),
   path(r'users/delete/<int:user_id>', views.deleteUser, name='user_delete'),
   path(r'recover-password', views.recoverPassword, name='recover_password'),
]