from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
  
    email = models.EmailField(_('email address'), unique=True) # changes email to unique and  false
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50, blank=True, null=True)
    username = models.CharField(_("user name"), unique=False, max_length=50, blank=True, null=True)
   
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    email_otp_expiry = models.DateTimeField(_("otp expiry"), auto_now=False, auto_now_add=False, blank=True, null=True)
    email_otp_resend = models.DateTimeField(_("email otp resend"), auto_now=False, auto_now_add=False, blank=True, null=True)
    email_otp_try = models.CharField(_("email otp try"),max_length=2, default=0)
    email_validated = models.BooleanField(default=False)

    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    profile_picture = models.ImageField(
        _('profile picture'), 
        upload_to="profile_images/",
        blank=True,
        null=True
    )
    
    bio = models.TextField(_('Bio'), max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name',  'username' ]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
