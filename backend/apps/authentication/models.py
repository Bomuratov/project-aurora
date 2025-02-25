from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import validate_email
from django.conf import settings
from core import utils
from apps.authentication.utils.constantas import RESOURCE, PERMISSIONS, VIEW, MENU


class VendorManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have a username")
        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_active = True
        user.is_staff = True
        user.is_manager = True
        user.is_supervisor = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, validators=[utils.USERNAME_VALIDATOR])
    phone = models.CharField(
        max_length=14,
        validators=[utils.UZB_PHONE_VALIDATOR],
        null=True,
        blank=True,
    )
    email = models.EmailField(blank=True, null=True, unique=True)
    code = models.CharField(max_length=6, null=True, unique=True)
    code_expiry = models.DateTimeField(blank=True, null=True)
    max_code_try = models.CharField(
        max_length=2, default=settings.MAX_CODE_TRY, null=True
    )
    code_max_out = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_supervisor = models.BooleanField(default=False)
    user_registered_at = models.DateTimeField(auto_now_add=True, editable=False)
    chat_id = models.BigIntegerField(null=True, blank=True)

    USERNAME_FIELD = "email"
    objects = VendorManager()

    def __str__(self):
        return self.email


class Roles(models.Model):
    action = models.CharField(max_length=100, choices=PERMISSIONS, default=VIEW)
    resource = models.CharField(max_length=255, choices=RESOURCE, default=MENU)
    perms = models.JSONField(null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if self.role and self.permission:
            permissions = []
            for per in self.permission:
                ...


# class UserLocation(models.Model):
#     user_id = models.ForeignKey("authentication.Usermodel", on_delete=models.CASCADE, null=True, blank=True)
#     long = models.CharField(max_length=255, null=True, blank=True)
#     lat = models.CharField(max_length=255, null=True, blank=True)


#     def __str__(self):
#         return str(self.user_id)
