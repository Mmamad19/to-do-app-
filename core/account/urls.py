from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='account'
urlpatterns = [

    path('signin/',views.SignUpView.as_view(),name='signin'),
    path('',include('django.contrib.auth.urls')),
    path('api/v1/',include('account.api.v1.urls'))
]