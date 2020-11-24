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
   path(r'change-password', views.changePassword, name='change_password'),
   path(r'check-password', views.checkCode, name='check_password'),
   path(r'mastografias/analyze', views.analyzeMastografia, name='mastografia_analyze'),
   path(r'mastografias/result/<int:mastografia_id>', views.getMastografia, name='mastografia_get_result'),
   path(r'mastografias/list/<int:usuario_id>', views.getMastografias, name='mastografia_get_list'),
]