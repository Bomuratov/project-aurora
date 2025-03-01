from rest_framework import serializers
from product.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    photo = serializers.FileField(required=False)

    class Meta:
        model = Menu
        fields = "__all__"