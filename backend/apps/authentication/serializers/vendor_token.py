from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from authentication.backend.authenticator import UsernameAuthBackend

class VendorTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавляем данные в payload токена
        token['is_user'] = user.is_user
        token['is_vendor'] = user.is_vendor

        return token
    
    def validate(self, attrs):
        user = UsernameAuthBackend.authenticate(
            request=self.context['request'],
            username=attrs.get('email'),
            password=attrs.get('password')
        )
        print(user)
        if not user or not user.is_vendor:
            raise serializers.ValidationError("Вы не являетесь вендором")
        
        refresh = self.get_token(user)
        return {'access': str(refresh.access_token), 'refresh': str(refresh)}