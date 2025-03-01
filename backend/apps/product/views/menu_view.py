from rest_framework import viewsets
from drf_spectacular.utils import extend_schema 
from django_filters import rest_framework as filters
from product.models import Menu
from product.serializers.menu_serializer import MenuSerializer

@extend_schema(tags=['Menu'])
class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['restaurant__name']
