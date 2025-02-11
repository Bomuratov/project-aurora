from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import viewsets


class CartViewSet(viewsets.ViewSet):
    def retrieve_cart(self, request):
        user_id = request.user.id
        cart_data = cache.get(f'cart_{user_id}', {})
        return Response(cart_data)

    def add_to_cart(self, request):
        user_id = request.user.id
        cart_data = cache.get(f'cart_{user_id}', {})

        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        if product_id in cart_data:
            cart_data[product_id] += quantity
        else:
            cart_data[product_id] = quantity

        cache.set(f'cart_{user_id}', cart_data, timeout=86400)  # Хранение 24 часа
        return Response(cart_data)

    def clear_cart(self, request):
        user_id = request.user.id
        cache.delete(f'cart_{user_id}')
        return Response({"message": "Cart cleared"})

# class OrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

#     def create(self, request, *args, **kwargs):
#         user_id = request.user.id
#         cart_data = cache.get(f'cart_{user_id}', {})

#         if not cart_data:
#             return Response({"error": "Cart is empty"}, status=400)

#         order = Order.objects.create(user=request.user, status='pending')
#         for product_id, quantity in cart_data.items():
#             order.items.add(product_id, through_defaults={'quantity': quantity})

#         order.save()
#         cache.delete(f'cart_{user_id}')  # Очищаем корзину после заказа
#         return Response(OrderSerializer(order).data)
