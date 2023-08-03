from django.urls import path ,include
from . import views
#from rest_framework.authtoken.views import ObtainAuthToken 

app_name='api-v1'
urlpatterns = [
    #registration
    path('registration/',views.RegistrationApiView.as_view(),name='registration'),
    #token login
    path('token/login/',views.CustomAuthToken.as_view(),name='token-login'),
    path('token/logout/',views.CustumDiscardAuthToken.as_view(),name='token-logout')
]   
