from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema 
from restaurant.models import Restaurant
from restaurant.serializers.restaurant_serializer import RestaurantSerializer


@extend_schema(tags=['Restaurant'])
class RestaurantView(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "name"
    
