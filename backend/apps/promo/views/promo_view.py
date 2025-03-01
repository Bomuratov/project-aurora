from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from promo.models import Promo
from promo.serializers.promo_serializer import PromoSerializer


class PromoView(ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["restaurant__name"]
    lookup_field = "pk"