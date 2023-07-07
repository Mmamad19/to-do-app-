from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager)
from django.dispatch import receiver
from django.db.models.signals import post_save
#creating user and superuser
class usermanger(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError('email recuired')
        email=self.normalize_email(email=email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('user must be staff')
        if extra_fields.get('is_active') is not True:
            raise ValueError('user must be active')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('user must be super user')
        return self.create_user(email=email,password=password,**extra_fields)

#user fields
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    first_name=models.CharField(max_length=255)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    object=usermanger()

    def __str__(self):
        return self.email

class profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    image=models.ImageField(blank=True,null=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

@receiver(post_save,sender=User)
def save_porf(sender,instance,created,**kwg):
    if created:
        profile.objects.create(user=instance)

    