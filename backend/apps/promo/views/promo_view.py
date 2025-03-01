from rest_framework.viewsets import ModelViewSet
from apps.promo.models import Promo
from apps.promo.serializers.promo_serializer import PromoSerializer


class PromoView(ModelViewSet):
    queryset = Promo.objects.all()