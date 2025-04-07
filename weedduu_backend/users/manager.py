from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext as _
from random import randint
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from .mail_templates import mail_template

class CustomUserManager(UserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, email,  phone_number,password, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))

        if '@' not in email:
            raise ValueError(_("Invalid email format"))

        if not phone_number:
            raise ValueError(_("Users must have a valid phone number."))

        if self.model.objects.filter(phone_number=phone_number).exists():
            raise ValueError(_("Phone number is already used. Try to login."))

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        if not extra_fields.get('is_superuser', False):
            otp = randint(100001, 999999)
            email_body = mail_template(email, otp)
            
            try:
                send_mail(
                    'Email Verification',
                    email_body,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                user.email_otp = otp
                user.email_otp_try = 1
                user.email_otp_expiry = timezone.now() + timedelta(minutes=1440)
                user.email_otp_resend = timezone.now() + timedelta(minutes=2)
            except Exception as e:
                raise ValidationError(_("Failed to send verification email"))

        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        
        if 'phone_number' not in extra_fields:
            raise ValueError(_("Superuser must have a phone number."))
            
        return self.create_user(email, password, **extra_fields)