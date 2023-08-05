from rest_framework import serializers
from ...models import User,profile
from django.core import exceptions
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import exceptions, serializers
from rest_framework.exceptions import ValidationError

class RegistrationApiSerializer(serializers.ModelSerializer):
    password1=serializers.CharField(max_length=255,write_only=True)
    class Meta:
        model=User
        fields=['email','password','password1']

    def validate(self, attrs):
        if attrs.get('password')!=attrs.get('password1'):
            raise serializers.ValidationError({'detail':'password doesnt match'})
        
        try:
            validate_password(attrs.get('password'))
        
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'email':list(e.messages)})
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('password1',None)
        return User.object.create_user(validated_data)

class CustumAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
            if not user.is_verified():
                 raise serializers.ValidationError({'detail':'user is not verified'})
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        if not self.user.is_verified():
                 raise serializers.ValidationError({'detail':'user is not verified'})
        valitaed_data= super().validate(attrs)
        return valitaed_data

class ChangePasswordApiSerializer(serializers.Serializer):
    old_password=serializers.CharField(required=True)
    now_password=serializers.CharField(required=True)
    now_password1=serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('now_password')!=attrs.get('now_password1'):
            raise serializers.ValidationError({'detail':'password doesnt match'})
        
        try:
            validate_password(attrs.get('now_password'))
        
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'now_password':list(e.messages)})
        return super().validate(attrs)


class ProfileApiSerializer(serializers.ModelSerializer):
    email=serializers.CharField(source='user.email',read_only=True)
    class Meta:
        model=profile
        fields=['id','email','first_name','last_name','image']
        read_only_fields=['email']
    
