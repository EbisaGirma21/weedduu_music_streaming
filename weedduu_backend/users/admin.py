from django.contrib import admin
from django.apps import AppConfig

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CustomUser'

admin.site.register(User)