from rest_framework import viewsets
from apps.product.models import Menu
from drf_spectacular.utils import extend_schema 
from apps.product.serializers.menu_serializer import MenuSerializer

@extend_schema(tags=['Menu'])
class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
