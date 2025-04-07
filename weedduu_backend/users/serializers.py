from rest_framework import serializers
from .models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer, UserSerializer
from django.core.validators import RegexValidator





User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, allow_blank=True, required=False)
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'username', 'last_name', 'phone_number', 'date_of_birth', 'profile_picture', 'bio', 'country', 'password')
        read_only_fields = ('id',)

    def validate_password(self, value):
        if value is not None:
            validate_password(value)
        return value
    
class CustomUserUpdateSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture', 'bio', 'country')
        read_only_fields = ('id', 'email', 'phone_number')

    def is_valid(self, raise_exception=False):
        const = super().is_valid(raise_exception)
        
        print("is_valid() method is called to validate the data")
        return const

class CustomUserSerializer(UserSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
            'email_otp': {'write_only': True},
            'phone_otp': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class CustomUserTokens(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

class UserSendOTPSerializer(serializers.Serializer):
    phoneNumber = PhoneNumberField()

class EmailSendOTPSerializer(serializers.Serializer):
    email = serializers.CharField()

class UserVerifyOTPSerializer(serializers.Serializer):
    phoneNumber = PhoneNumberField()
    otpCode = serializers.CharField(
        max_length=6,
        error_messages={
            'invalid': 'OTP code must be exactly 6 characters long.',
        }
    )

    def validate_otpCode(self, value):
        if len(value) != 6:
            raise serializers.ValidationError('OTP code must be exactly 6 characters long.')
        return value

class UserVerifyOTPCodeSerializer(serializers.Serializer):
    email = serializers.CharField()
    otpCode = serializers.CharField(
        max_length=6,
        error_messages={
            'invalid': 'OTP code must be exactly 6 characters long.',
        }
    )

    def validate_otpCode(self, value):
        if len(value) != 6:
            raise serializers.ValidationError('OTP code must be exactly 6 characters long.')
        return value
    

class UserViewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "phone_number", "date_of_birth", "profile_picture", "bio", "country")
        read_only_fields = ('id',)

    def validate_password(self, value):

        if value is not None:
            validate_password(value)
        return value
    