from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

class ShopkeeperManager(BaseUserManager):
    def create_user(self,email=None,phone = None , password = None):
        if not email and not phone:
            raise ValueError("Email or Phone required")
        
        user = self.model(email=email,phone=phone)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email=None,phone = None , password = None):
        user = self.create_user(email=email,phone=phone,password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user




class Shopkeeper(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15,unique=True,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    address = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShopkeeperManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email or self.phone
