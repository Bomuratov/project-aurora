from rest_framework.viewsets import ModelViewSet
from restaurant.models import Restaurant
from restaurant.serializers.vendor_serializer import VendoerSerializer


class VendorView(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = VendoerSerializer
    lookup_field = "pk"
    
