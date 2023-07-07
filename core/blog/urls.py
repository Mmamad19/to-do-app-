from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='blog'
urlpatterns = [
    path('post/',views.postview.as_view(),name='post'),
    path('post/create/',views.create_data.as_view(),name='createdata'),
    path('post/<int:pk>/edit/',views.edit.as_view(),name='edit'),
    path('post/<int:pk>/delete/',views.delete.as_view(),name='delete'),
]