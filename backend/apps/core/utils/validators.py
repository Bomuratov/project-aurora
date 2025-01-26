from django.core.validators import RegexValidator

UZB_PHONE_VALIDATOR = RegexValidator(regex=r"^(\+998)(\d{9})$", message="Введённый номер телефона неправильно. Пример +998(XX)XXX-XX-XX")
USERNAME_VALIDATOR = RegexValidator(regex=r"^[a-z0-9-]+$", message="Имя пользователя может содержать только буквы неижнего регистра, цифры и дефис.")
