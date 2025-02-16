from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.views.cart_view import CartViewSet

router = DefaultRouter()


cart_list = CartViewSet.as_view({
    'get': 'retrieve_cart',
    'post': 'add_to_cart',
    'delete': 'clear_cart',
})

urlpatterns = [
    path('cart/', cart_list, name='cart'),

]
