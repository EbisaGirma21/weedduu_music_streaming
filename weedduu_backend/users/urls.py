from django.urls import path
from .views import create_user, get_users, login, signup, user_detail

urlpatterns = [
    path('users/sign-up/', signup, name='signup'),
    path('users/login/',login, name='login'),
    path('users/',get_users, name='get_users'),
    path('users/create/',create_user, name='create'),
    path('users/<int:pk>/',user_detail, name='user_detail'),
]
