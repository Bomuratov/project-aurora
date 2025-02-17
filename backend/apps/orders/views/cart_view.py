from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema 

@extend_schema(tags=['Cart actions'])
class CartViewSet(viewsets.ViewSet):
    def retrieve_cart(self, request):
        user_id = request.user.id
        cart_data = cache.get(f'cart_for_{user_id}', {})
        return Response(cart_data)

    def add_to_cart(self, request):
        user_id = request.user.id
        cart_key = f'cart_for_{user_id}'
        
        # Получаем существующую корзину (если нет, то создаем пустую)
        cart_data = cache.get(cart_key, {})
        
        # Если корзина новая, инициализируем общий total_price
        if "total_price" not in cart_data:
            cart_data["total_price"] = 0

        product_id = request.data.get('product_id')
        product_name = request.data.get('product_name')
        product_price = request.data.get('product_price')
        quantity = int(request.data.get('quantity', 1))
        lat = request.data.get('lat')
        product_id = request.data.get('product_id')
        product_id = request.data.get('product_id')
        product_id = request.data.get('product_id')
        product_id = request.data.get('product_id')

        # if not (product_id and product_name and product_price):
        #     return Response({"error": "Missing product data"}, status=400)

        # Проверяем, есть ли товар в корзине
        if product_id in cart_data:
            old_quantity = cart_data[product_id]["quantity"]
            new_quantity = max(0, old_quantity + quantity)  # Не позволяем quantity < 0

            # Вычисляем разницу в цене
            price_diff = (new_quantity - old_quantity) * product_price

            if new_quantity == 0:
                # Удаляем товар, если количество стало 0
                del cart_data[product_id]
            else:
                # Обновляем количество и цену
                cart_data[product_id]["quantity"] = new_quantity
                cart_data[product_id]["total_price"] = new_quantity * product_price

        else:
            if quantity > 0:  # Добавляем только если количество > 0
                cart_data[product_id] = {
                    "id": product_id,
                    "name": product_name,
                    "price": product_price,
                    "quantity": quantity,
                    "total_price": quantity * product_price
                }
                price_diff = quantity * product_price
            else:
                price_diff = 0  # Если товар не был в корзине и quantity <= 0, игнорируем

        # Обновляем общий total_price
        cart_data["total_price"] = max(0, cart_data["total_price"] + price_diff)

        # Если в корзине остался только `total_price`, очищаем её
        if len(cart_data) == 1 and "total_price" in cart_data:
            cart_data = {}
        cart_data["lat"]
        cart_data["long"]
        cart_data["user_id"]
        cart_data["restaurant"] = 3
        cart_data["is_online"] = True
        # Обновляем кеш на 24 часа
        cache.set(cart_key, cart_data, timeout=86400)

        return Response(cart_data)

    
    def clear_cart(self, request):
        user_id = request.user.id
        cache.delete(f'cart_for_{user_id}')
        return Response({"message": "Корзинка очищено"})

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


"""


{
    "product_id": 2,
    "product_name": "Burger",
    "product_price": 15000,
    "quantity": 4
}


"""

"""

{
    "total_price": 120000,
    "2": {
        "id": 2,
        "name": "Burger",
        "price": 15000,
        "quantity": 6,
        "total_price": 90000
    },
    "1": {
        "id": 1,
        "name": "Pizza",
        "price": 15000,
        "quantity": 2,
        "total_price": 30000
    }
}

"""