from rest_framework import serializers
from apps.promo.models import Promo


class PromoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promo
        fields = "__all__"
