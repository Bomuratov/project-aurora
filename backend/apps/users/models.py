from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import validate_email
from django.conf import settings
from core import utils



class UserModel(models.Model):
    username = models.CharField(max_length=255, validators=[utils.USERNAME_VALIDATOR], unique=True)
    email = models.CharField(max_length=100, validators=[validate_email])
    phone = models.CharField(
        unique=True,
        max_length=14,
        validators=[utils.UZB_PHONE_VALIDATOR],
        null=True,
        blank=True,
    )
    code = models.CharField(max_length=6)
    code_expiry = models.DateTimeField(blank=True, null=True)
    max_code_try = models.CharField(max_length=6, default=settings.MAX_CODE_TRY)
    code_max_out = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_robot = models.BooleanField(default=False)
    user_registered_at = models.DateTimeField(auto_now_add=True, editable=False)
    chat_id = models.BigIntegerField(null=True, blank=True)

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
