from rest_framework import viewsets
from apps.product.models import Menu
from apps.product.serializers.menu_serializer import MenuSerializer

class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
