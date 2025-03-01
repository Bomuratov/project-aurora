from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from promo.models import Promo
from promo.serializers.promo_serializer import PromoSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["User register"])
class PromoView(ModelViewSet):
    queryset = Promo.objects.all()
    serializer_class = PromoSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ["restaurant__name"]
    lookup_field = "pk"
