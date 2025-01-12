from rest_framework.viewsets import ModelViewSet
from vendor.models import Vendor
from vendor.serializers.vendor_serializer import VendoerSerializer


class VendorView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendoerSerializer
    lookup_field = "pk"
    
