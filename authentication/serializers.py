from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=64, min_length=8, write_only=True)
    id=serializers.ReadOnlyField()
    class Meta:
        model= User
        fields = ['email','password','full_name','id']

    def validate(self, attrs):

        email = attrs.get('email','')
        full_name = attrs.get('full_name','')
        


        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data) #creates a new user on successful registration

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()
    password=serializers.CharField(max_length=64, min_length=8, write_only=True)
    tokens=serializers.CharField(read_only=True)

    class Meta:
        model= User
        fields = ['email','password','id','tokens']

    def validate(self, attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        
        user=auth.authenticate(email=email,password=password)
        if not user:
            raise AuthenticationFailed('Invalid Credentials')
        if not user.is_active:
            raise AuthenticationFailed('Inactive User')
        
        return {
            'email':user.email,
            'tokens':user.tokens,
            'id':user.id
        }