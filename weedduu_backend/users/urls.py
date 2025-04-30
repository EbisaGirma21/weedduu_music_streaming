from django.urls import path
from .views import  get_users, login, signup, user_detail, verify_otp

urlpatterns = [
    path('users/sign-up/', signup, name='signup'),
    path('users/verify-otp/', verify_otp, name='verify_otp'),
    path('users/login/',login, name='login'),
    path('users/',get_users, name='get_users'),
    path('users/<int:pk>/',user_detail, name='user_detail'),
]
