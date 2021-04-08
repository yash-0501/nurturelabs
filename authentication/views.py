from django.shortcuts import render
from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User

# Create your views here.
class RegistrationView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self,request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user=User.objects.get(email=serializer.data['email'])
        token = RefreshToken.for_user(user).access_token
        user_data = {"id":serializer.data["id"],"token":str(token)}

        return Response(user_data,status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        response = Response()
        token = serializer.data["tokens"]
        response.set_cookie(key='jtw', value=token)
        user_data = {"id":serializer.data["id"],"tokens":token}
        return Response(user_data,status=status.HTTP_200_OK)
