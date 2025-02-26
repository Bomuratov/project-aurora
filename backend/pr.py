# import requests

# headers = {
#         'Content-Type': 'application/json',
#     }
# def send_code(phone, code):
#     url = "https://brainy-hummingbird-gbteam-4548a45b.koyeb.app/send_code/"
#     json={
#         "user_id": phone,
#         "data": code
#     }
#     try:
#         response = requests.post(url, json=json, headers=headers)
#         response.raise_for_status()
#         return response.json()

#     except requests.exceptions.RequestException as e:
#         print(f'Произошла ошибка: {e}')
#         print(f'Статус: {response.status_code}, Тело ответа: {response.text}')
#         return None
    
# print(send_code(phone="998881836222", code="123456"))



# """
# order.json

# {
#     "total_price": 120000,
#     "user_id": 1,
#     "restaurant": 3
#     "2": {
#         "id": 2,
#         "name": "Burger",
#         "price": 15000,
#         "quantity": 6,
#         "total_price": 90000
#     },
#     "1": {
#         "id": 1,
#         "name": "Pizza",
#         "price": 15000,
#         "quantity": 2,
#         "total_price": 30000
#     }
# }



"""



import django
import os

# Указываем путь к settings.py
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.authentication.models import UserModel
from apps.restaurant.models import Restaurant
from apps.product.models import Category, Menu
from django.db import transaction

# Подключаем старую базу
import psycopg2

OLD_DB = {
    "NAME": "aurora",
    "USER": "aurora",
    "PASSWORD": "admin",
    "HOST": "localhost",
    "PORT": "5432",
}

conn = psycopg2.connect(
    dbname=OLD_DB["NAME"],
    user=OLD_DB["USER"],
    password=OLD_DB["PASSWORD"],
    host=OLD_DB["HOST"],
    port=OLD_DB["PORT"],
)
cursor = conn.cursor()


@transaction.atomic
def migrate_users():
    cursor.execute("SELECT id, username, email, is_active FROM auth_user;")
    print("cursor.execute - ok")
    users = cursor.fetchall()

    print("users = cursor.fetchall() - ok")
    for user in users:
        user_id, username, email, is_active = user
        print("цикл запушен")
        if not UserModel.objects.filter(email=email).exists():
            print("цикл запушен x2")
            UserModel.objects.create(
                username=username,
                email=email,
                is_active=is_active,
            )
            print("проверку прошли ок")
    print("✅ Users migrated successfully")


@transaction.atomic
def migrate_restaurants():
    cursor.execute("SELECT id, user_id, name, adress, telegram, instagramm FROM restaurant_restaurant;")
    restaurants = cursor.fetchall()

    for rest in restaurants:
        rest_id, user_id, name, address, telegram, instagram = rest
        admin = UserModel.objects.filter(id=user_id).first()  # Связываем с новым пользователем
        Restaurant.objects.create(
            admin=admin,
            name=name,
            adress=address,
            telegram_link=telegram,
            instagram_link=instagram,
        )
    print("✅ Restaurants migrated successfully")


@transaction.atomic
def migrate_categories():
    cursor.execute("SELECT id, restaurant_id, name, order FROM restaurant_category;")
    categories = cursor.fetchall()

    for cat in categories:
        cat_id, restaurant_id, name, order = cat
        restaurant = Restaurant.objects.filter(id=restaurant_id).first()
        if restaurant:
            Category.objects.create(
                restaurant=restaurant,
                name=name,
                order=order,
            )
    print("✅ Categories migrated successfully")


@transaction.atomic
def migrate_menus():
    cursor.execute("SELECT id, name, description, price, category_id, restaurant_id FROM restaurant_menu;")
    menus = cursor.fetchall()

    for menu in menus:
        menu_id, name, description, price, category_id, restaurant_id = menu
        restaurant = Restaurant.objects.filter(id=restaurant_id).first()
        category = Category.objects.filter(id=category_id).first()

        if restaurant and category:
            Menu.objects.create(
                name=name,
                description=description,
                price=price,
                category=category,
                restaurant=restaurant,
            )
    print("✅ Menus migrated successfully")


if __name__ == "__main__":
    migrate_users()
    migrate_restaurants()
    migrate_categories()
    migrate_menus()
    print("🎉 Data migration completed successfully!")



# {
#     "order": {
#         "id" : 1,
#         "created_at" : "date-time",
#         "updated_at" : "date-time",
#         "products" : [ {
#             "id": 1,
#             "price": 12000,
#             "quantity": 2,
#             "total_price": 24000
#         },
#         {
#             "id": 2,
#             "price": 10000,
#             "quantity": 2,
#             "total_price":20000
#         },
#         {
#             "id": 3,
#             "price": 5000,
#             "quantity": 2,
#             "total_price": 10000
#         }
#     ],
#         "total_price": 54000,
#         "lat": "647328413948",
#         "long": "23678492965728",
#         "user_id": 1,
#         "restaurant":3

#     }
# }

"""