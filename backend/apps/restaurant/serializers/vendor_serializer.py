from rest_framework.serializers import ModelSerializer
from restaurant.models import Restaurant


class VendoerSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"