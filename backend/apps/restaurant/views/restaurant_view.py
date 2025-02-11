from rest_framework.viewsets import ModelViewSet
from restaurant.models import Restaurant
from apps.restaurant.serializers.restaurant_serializer import RestaurantSerializer


class RestaurantView(ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "pk"
    
