from datetime import timedelta
import random
from rest_framework import viewsets, decorators, response, status
from django.conf import settings
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from authentication.models import UserModel
from apps.authentication.serializers.user_register_serializer import UserSerializer

@extend_schema(tags=['User register'])
class UserView(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    lookup_field = "pk"

    @decorators.action(detail=True, methods=["PATCH"])
    def verification(self, request, pk=None):
        instance = self.get_object()
        now = timezone.now()
        print(f"request - {now} type - {type(now)}")
        print(f"database - {instance.code_expiry} type - {type(instance.code_expiry)}")

        if not instance.code_expiry:
            return response.Response({
            "message": "Похоже вы уже верифицированы", "code": 1
        }, status=status.HTTP_302_FOUND)

        if now >= instance.code_expiry:
            return response.Response({"message": "Срок действия кода истёк", "code": 2}, status=status.HTTP_400_BAD_REQUEST)
        
        if not request.data.get("code"):
            return response.Response({"message": "Введите проверочный код", "code": 3}, status=status.HTTP_404_NOT_FOUND)
        
        code = request.data.get("code")
        print(f"request - {now} type - {type(now)}")
        print(f"database - {instance.code_expiry} type - {type(instance.code_expiry)}")

        if int(code) != int(instance.code):
            return response.Response({"message": "Вы неправильно ввели проверочный код", "code": 4}, status=status.HTTP_404_NOT_FOUND)
        

        
        if (
            not instance.is_active
            and int(instance.code) == int(code)
            and instance.code_expiry > now
        ):
            instance.is_active = True
            instance.is_user = True
            instance.code_expiry = None
            instance.max_code_try = settings.MAX_CODE_TRY
            instance.code_max_out = None
            
            instance.save()
            return response.Response({
                "message": "Пользователь успешно верифицирован", "code": 6}, status=status.HTTP_201_CREATED
            )
        
        return response.Response({
            "message": "Непревиденна ошибка пользователь уже верифицирован или код верификации не требуется", "code": 5
        }, status=status.HTTP_409_CONFLICT)
    

    @decorators.action(detail=True, methods=["PATCH"])
    def generate(self, request, pk=None):
        instance = self.get_object()
        now = timezone.now()

        if instance.is_active:
            return response.Response({
                "message": "Похоже вы уже верифицированы", "code": 10
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if int(instance.max_code_try) == 0 and instance.code_max_out > now:
            return response.Response({
                "message": "Вы много раз запросили код верификации попробуйте через 2 часа или 120 минут", "code": 11 
            }, status=status.HTTP_400_BAD_REQUEST)
        
        max_code_try = int(instance.max_code_try) - 1
        instance.code_expiry = timezone.now() + timedelta(minutes=30) # срок действия кода 30 минут
        instance.code = random.randint(100000, 999999)
        instance.max_code_try = max_code_try

        if int(instance.max_code_try) == 0:
            instance.code_max_out = timezone.now() + timedelta(hours=1)

        if instance.max_code_try == -1:
            instance.max_code_try = settings.MAX_CODE_TRY
            instance.code_max_out = None
            
        instance.save()
        # send_code(instance.phone, code)
        return response.Response({
            "message": f"Код верификации успешно отправлен на ваш номер {instance.phone} полученный код нужно ввести тут https://localhost:8000/api/v1/auth/{instance.pk}/verification/", "error_code": 0
        }, status=status.HTTP_201_CREATED)