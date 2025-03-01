import random
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
from rest_framework import serializers
from authentication.models import UserModel
from authentication.utils.send_code import send_code
from authentication.exceptions.validate_exception import ValidateErrorException
from authentication.utils.unique_validator import UniqueValidator
from core import utils


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[
            UniqueValidator(
                queryset=UserModel.objects.all(),
                message="Пользователь с такими данными уже существует",
                code="3",
            )
        ]
    )
    phone = serializers.CharField(
        validators=[
            utils.UZB_PHONE_VALIDATOR,
            UniqueValidator(
                queryset=UserModel.objects.all(),
                message="Пользователь с такими данными уже существует.",
                code="3",
            ),
        ]
    )
    username = serializers.CharField(
        validators=[
            utils.USERNAME_VALIDATOR,
            UniqueValidator(
                queryset=UserModel.objects.all(),
                message="Пользователь с такими данными уже существует.",
                code="3",
            ),
        ]
    )
    password_1 = serializers.CharField(
        write_only=True,
        min_length=settings.PASSWORD_MIN_LENGHT,
        error_messages={
            "min_length": f"Парол должен быть больше {settings.PASSWORD_MIN_LENGHT} символов"
        },
    )
    password_2 = serializers.CharField(
        write_only=True,
        min_length=settings.PASSWORD_MIN_LENGHT,
        error_messages={
            "min_length": f"Парол должен быть больше {settings.PASSWORD_MIN_LENGHT} символов"
        },
    )

    bot_link = serializers.SerializerMethodField()

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "email",
            "phone",
            "password_1",
            "password_2",
            "user_registered_at",
            "bot_link",
        ]
        read_only_fields = ("id", "user_registered_at", "code")

    def get_bot_link(self, obj):
        return getattr(obj, "bot_link", None)

    def validate(self, attrs):
        if attrs["password_1"] != attrs["password_2"]:
            raise ValidateErrorException(detail="Пароли не совпадают", code=2)
        return attrs

    def create(self, validated_data):
        code = random.randint(100000, 999999)
        code_expiry = timezone.now() + timedelta(
            minutes=30  # срок дейтвия кода 30 минут или 30 минут
        )  
        user = UserModel.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            code=code,
            code_expiry=code_expiry,
            max_code_try=settings.MAX_CODE_TRY,
        )
        user.set_password(validated_data["password_1"])
        user.is_active = False
        user.is_staff = False
        response_code = send_code(phone=validated_data["phone"], code=str(code))
        user.save()
        user.bot_link = response_code.get("detail", None)
        return user