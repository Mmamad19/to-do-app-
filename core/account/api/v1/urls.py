from django.urls import path ,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)
#from rest_framework.authtoken.views import ObtainAuthToken 

app_name='api-v1'
urlpatterns = [
    #registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    path('test-email/',views.TestSendEmail.as_view(),name='send-email'),
    #token login
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustumDiscardAuthToken.as_view(),name='token-logout'),
    #jwt
    path('jwt/create/',views.CustomTokenObtainPairView.as_view(),name='teken-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #change password
    path('change-password/',views.ChangePasswordApiView.as_view(),name='change-password'),
    #profile
    path('profile/',views.ProfileApiView.as_view(),name='profile'),
    #activation
]   
