from rest_framework import generics 
from .serializer import RegistrationApiSerializer,CustumAuthTokenSerializer,CustomTokenObtainPairSerializer,ChangePasswordApiSerializer,ProfileApiSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from ...models import User,profile
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

class RegistrationApiView(generics.GenericAPIView):
    serializer_class=RegistrationApiSerializer

    def post(self,request,*arges,**kwatgs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={'email':serializer.validated_data['email']}
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CustomAuthToken(ObtainAuthToken):
    serializer_class=CustumAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class CustumDiscardAuthToken(APIView):
    permission_classes=[IsAuthenticated]

    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
        serializer_class = ChangePasswordApiSerializer
        model = User
        permission_classes = [IsAuthenticated]
        
        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                # Check old password
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
                # set_password also hashes the password that the user will get
                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()
                
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'Password updated successfully',
                    'data': []
                }

                return Response(response)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveAPIView):
    serializer_class=ProfileApiSerializer
    queryset=profile.objects.all()
    permission_classes=[IsAuthenticated]

    def get_object(self):
        queryset=self.get_queryset()
        obj=get_object_or_404(queryset,self.request.user)
        return obj




class TestSendEmail(generics.GenericAPIView):
    def post(self,request,*arges,**kwarges):
        
        send_mail(
                "Subject here",
                "Here is the message.",
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )
        return Response('email sent')