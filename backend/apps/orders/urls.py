from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.orders.views.cart_view import CartViewSet

router = DefaultRouter()

# Регистрируем OrderViewSet (если используется ModelViewSet)
# router.register(r'orders', OrderViewSet, basename='order')

# Маршруты для корзины (CartViewSet вручную, так как он ViewSet, а не ModelViewSet)
cart_list = CartViewSet.as_view({
    'get': 'retrieve_cart',
    'post': 'add_to_cart',
    'delete': 'clear_cart',
})

urlpatterns = [
    path('cart/', cart_list, name='cart'),
    # path('', include(router.urls)),  # Добавляем маршруты заказов
]
