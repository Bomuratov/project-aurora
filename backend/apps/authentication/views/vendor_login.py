from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema
from ..serializers.vendor_token import VendorTokenObtainPairSerializer


@extend_schema(tags=['Vendor login'])
class VendorLoginView(TokenObtainPairView):
    serializer_class = VendorTokenObtainPairSerializer