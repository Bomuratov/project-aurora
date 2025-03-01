from rest_framework.viewsets import ModelViewSet
from promo.models import Promo
from promo.serializers.promo_serializer import PromoSerializer


class PromoView(ModelViewSet):
    queryset = Promo.objects.all()