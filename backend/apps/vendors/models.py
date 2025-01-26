from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import validate_email
from django.conf import settings
from core import utils


class VendorManager(BaseUserManager):

    def create_user(self, username, password=None):
        if not username:
            raise ValueError("User must have a username")
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_manager = True
        user.is_supervisor = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class VendorModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, validators=[utils.USERNAME_VALIDATOR], unique=True)
    phone_number = models.CharField(
        unique=True,
        max_length=14,
        validators=[utils.UZB_PHONE_VALIDATOR],
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    user_registered_at = models.DateTimeField(auto_now_add=True, editable=False)
    chat_id = models.BigIntegerField(null=True, blank=True)

    USERNAME_FIELD = "username"
    objects = VendorManager()

    def __str__(self):
        return self.username
