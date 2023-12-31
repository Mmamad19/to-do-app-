from django.contrib import admin
from django.contrib.auth.admin import (UserAdmin)
from .models import User,profile

#register models
class showdetail(UserAdmin):
    model=User
    list_display=('email','is_staff','is_active','is_verified','password')
    list_filter =('email','is_staff','is_active','is_verified',)
    search_fields=('email',)
    ordering=('email',)
    fieldsets = [
        (
            None,
            {
                "fields": ["email","password"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["is_staff", "is_active"],
        
            },
        ),
    ]
    add_fieldsets=      [  (
            None,
            {
                "fields": ["email","password1",'password2','is_staff','is_active','is_verified'],
            },
        )]

admin.site.register(User,showdetail)
admin.site.register(profile)
# Register your models here.
