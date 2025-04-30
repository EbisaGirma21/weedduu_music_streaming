from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from random import randint
from datetime import timedelta
import uuid, random
from jinja2 import Template
from .mail_templates import mail_template
from .serializers import CustomUserSerializer, CustomUserUpdateSerializer, UserVerifyOTPCodeSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError



User = get_user_model()  


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    random.seed(str(uuid.uuid4()))
    otpCode = randint(100001, 999999)

    email_body = mail_template(user.first_name, otpCode)
    jinja_template = Template(email_body)
    rendered_email_body = jinja_template.render()

    send_mail(
        'Login OTP Verification',
        '',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=rendered_email_body
    )
    user.email_otp = otpCode
    user.email_otp_expiry = timezone.now() + timedelta(minutes=2)
    user.email_otp_resend = timezone.now() + timedelta(minutes=1)
    user.email_otp_try = int(user.email_otp_try or 0) + 1
    user.save()

    return Response({
        "message": "OTP has been sent to your email. Please verify to complete login.",
        "otp_sent": True,
        "resend_available_at": str(user.email_otp_resend),
    }, status=status.HTTP_200_OK)
    
    
    
@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        try:
            user = User.objects.create_user(
                email=validated_data.get('email'),
                password=validated_data.get('password'),
                phone_number=validated_data.get('phone_number'),
                first_name=validated_data.get('first_name', ''),
                last_name=validated_data.get('last_name', ''),
                username=validated_data.get('username', ''),
                country=validated_data.get('country', ''),
                date_of_birth=validated_data.get('date_of_birth', None)
            )
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "user": CustomUserSerializer(user).data},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Something went wrong."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def verify_otp(request):
    serializer = UserVerifyOTPCodeSerializer(data=request.data)
    
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp_code = serializer.validated_data['otpCode']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if not user.email_otp or str(user.email_otp) != str(otp_code):
            return Response({'message': 'Invalid OTP code.'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.email_otp_expiry and timezone.now() > user.email_otp_expiry:
            return Response({'message': 'OTP code has expired.'}, status=status.HTTP_403_FORBIDDEN)

        # Clear OTP fields and activate the user
        user.email_otp = None
        user.email_otp_expiry = None
        user.email_otp_try = 0
        user.email_otp_resend = None
        user.email_validated = True
        user.is_active = True
        user.save()

        # Invalidate previous tokens
        try:
            for token in OutstandingToken.objects.filter(user=user):
                token.delete()
        except Exception as e:
            print("Token cleanup error:", e)

        # Generate new JWT tokens
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)

        serialized_user = CustomUserSerializer(user)

        return Response({
             'message': 'OTP verified successfully.',
            'user': serialized_user.data,
            'refresh': str(refresh),
            'access': access
        }, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    users = User.objects.filter(is_superuser=False)
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user= User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    if request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
            serializer = CustomUserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
@api_view(['PATCH', 'PUT', 'GET', 'POST'])
def page_not_found(request):
    return Response(data={'message': 'Page not found.'}, status=status.HTTP_404_NOT_FOUND)