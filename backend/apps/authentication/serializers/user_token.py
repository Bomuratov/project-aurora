from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from apps.authentication.backend.authenticator import PhoneAuthBackend


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем данные в payload токена
        token['is_user'] = user.is_user
        token['is_vendor'] = user.is_vendor

        return token

    def validate(self, attrs):
        user = PhoneAuthBackend.authenticate(
            request=self.context['request'],
            phone=attrs.get('username'),
            password=attrs.get('password')
        )
        
        if not user or user.is_vendor:
            raise serializers.ValidationError("Неправильный логин и пароль или пользователь не найден")
        
        refresh = self.get_token(user)
        return {'access': str(refresh.access_token), 'refresh': str(refresh)}
    

"""""
    +998881836222
    admin1234
"""""