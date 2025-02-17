from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema
from authentication.serializers.user_token import UserTokenObtainPairSerializer

@extend_schema(tags=['User login'])
class UserLoginView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
    


"""
{
	"phone": "+998881836222",
	"password":"admin1234"
}
"""