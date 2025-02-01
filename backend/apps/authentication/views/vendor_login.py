from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers.vendor_token import VendorTokenObtainPairSerializer


class VendorLoginView(TokenObtainPairView):
    serializer_class = VendorTokenObtainPairSerializer