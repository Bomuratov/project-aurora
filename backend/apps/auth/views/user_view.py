import datetime
import random
from rest_framework import viewsets, decorators, response, status
from django.conf import settings
from django.utils import timezone
from auth.models import UserModel
from auth.serializers.user_serializer import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    @decorators.action(detail=True, methods=["PATCH"])
    def verification(self, request, pk=None):
        instance = self.get_object()
        now = timezone.now()

        if now >= instance.code_expiry:
            raise response.Response({"message": " Срок действия кода истёк"})
        
        if not request.data.get("code"):
            raise response.Response({"message": "Введите проверочный код"})
        
        code = request.data.get("code")

        if code != instance.code:
            raise response.Response({"message": "Вы неправильно ввели ввели проверочный код"})
        
        if (
            not instance.is_active
            and instance.code == code
            and instance.code_expiry
            and instance.code_expiry < now
        ):
            instance.is_active = True
            instance.code_expiry = None
            instance.max_code_try = settings.MAX_CODE_TRY
            instance.code_max_out = None
            instance.save()
            return response.Response(
                "Пользователь успешно верифицирован", status=status.HTTP_201_CREATED
            )
        return response.Response({
            "message": "Непревиденна ошибка пользователь уже верифицирован или код верификации не требуется"
        })