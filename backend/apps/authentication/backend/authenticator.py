from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class PhoneAuthBackend:

    def __init__(self):
        pass

    @staticmethod
    def authenticate(request, phone=None, password=None):
        try:
            user = User.objects.get(phone=phone, is_user=True)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

class UsernameAuthBackend:

    def __init__(self):
        pass

    @staticmethod
    def authenticate(request, username=None, password=None):
        try:
            user = User.objects.get(username=username, is_vendor=True)

            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        
    @staticmethod
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None