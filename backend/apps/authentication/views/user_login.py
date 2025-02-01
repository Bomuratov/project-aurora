from rest_framework_simplejwt.views import TokenObtainPairView
from authentication.serializers.user_token import UserTokenObtainPairSerializer

class UserLoginView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    


"""
{
	"phone": "+998881836222",
	"password":"admin1234"
}
"""