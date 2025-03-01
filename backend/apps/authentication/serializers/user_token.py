from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authentication.exceptions.validate_exception import ValidateErrorException
from authentication.backend.authenticator import PhoneAuthBackend


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
            phone=attrs.get('email'),
            password=attrs.get('password')
        )
        
        if not user or user.is_vendor:
            raise ValidateErrorException(detail="Неправильный логин или пароль.", code=401)
        
        refresh = self.get_token(user)
        return {'access': str(refresh.access_token), 'refresh': str(refresh)}
    

"""""
    +998881836222
    admin1234
"""""