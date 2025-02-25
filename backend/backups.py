# import os
# import logging
# import requests
# import django
# import psycopg2
# from concurrent.futures import ThreadPoolExecutor
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
# django.setup()
# from django.db import transaction
# from django.core.files import File

# # Импорт моделей
# from apps.authentication.models import UserModel
# from apps.restaurant.models import Restaurant
# from apps.product.models import Category, Menu
# from django.db import connection
# from django.utils import timezone
# import uuid

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Путь к папке MEDIA_ROOT (укажи правильный путь)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"/restaurant_photos"

<<<<<<< HEAD
# Подключаем старую базу данных
OLD_DB = {
    "NAME": "aurora",
    "USER": "aurora",
    "PASSWORD": "admin",
    "HOST": "0.0.0.0",
    "PORT": "5432",
}
=======
# # Подключаем старую базу данных
# OLD_DB = {
#     "NAME": "aurora",
#     "USER": "aurora",
#     "PASSWORD": "admin",
#     "HOST": "localhost",
#     "PORT": "5432",
# }
>>>>>>> origin

# conn = psycopg2.connect(
#     dbname=OLD_DB["NAME"],
#     user=OLD_DB["USER"],
#     password=OLD_DB["PASSWORD"],
#     host=OLD_DB["HOST"],
#     port=OLD_DB["PORT"],
# )
# cursor = conn.cursor()

# # def download_image(url, folder):
# #     """Скачивает изображение и сохраняет в указанную папку с уникальным именем."""
# #     prefix = "https://aurora-api.uz/media/"
# #     full_url = prefix + url
    
# #     unique_filename = f"{uuid.uuid4().hex}.jpg"  # Генерируем уникальное имя файла
# #     save_path = os.path.join(BASE_DIR, folder, unique_filename)
# #     relative_path = os.path.join(folder, unique_filename)

# #     # Если файл уже скачан, пропускаем загрузку
# #     if os.path.exists(save_path):
# #         logging.info(f"✔ Файл уже существует: {save_path}")
# #         return relative_path

# #     try:
# #         response = requests.get(full_url, timeout=5)
# #         response.raise_for_status()

# #         os.makedirs(os.path.dirname(save_path), exist_ok=True)

# #         with open(save_path, "wb") as file:
# #             file.write(response.content)

# #         logging.info(f"✅ Фото загружено: {save_path}")
# #         return relative_path
# #     except requests.RequestException as e:
# #         logging.error(f"❌ Ошибка загрузки {full_url}: {e}")
# #         return None



# # @transaction.atomic
# # def migrate_users():
# #     cursor.execute("SELECT id, username, email, is_active FROM auth_user;")
# #     users = cursor.fetchall()
# #     email_counter = 1
# #     for user in users:
# #         user_id, username, email, is_active = user
# #         print("—————————————")
# #         print(f"Процесс для: ——> {username}, {email}")
# #         print("—————————————")

# #         if not email or email.strip() == "":
# #             safe_username = username.strip() if username else "user"
# #             print("—————————————")
# #             print("генерация фейл емаил")
# #             print("—————————————")
# #             email = f"{safe_username}_{email_counter}@mail.ru"
# #             email_counter += 1

# #         user_obj, created = UserModel.objects.get_or_create(
# #             id=user_id,
# #             username=username,
# #             is_vendor=True,
# #             code=123456+email_counter,
# #             code_expiry=timezone.now(),
# #             user_registered_at= timezone.now(),
# #             defaults={
# #                 "email": email,
# #                 "is_active": is_active,
# #             }
# #         )
# #         print(user_obj)
# #         print("—————————————")

# #         if created:
# #             print("—————————————")
# #             print(f"User {email} ——> uspex.")
# #             print("—————————————")
# #         else:
# #             print("—————————————")
# #             print(f"User {email} ——> uje yest.")
# #             print("—————————————")

# #     print("—————————————")
# #     print("Users - uspex")
# #     print("—————————————")


# # @transaction.atomic
# # def migrate_restaurants():
# #     """Переносит рестораны и загружает их фото асинхронно."""
# #     cursor.execute("SELECT id, user_id, name, adress, telegram, instagramm, logo, photo FROM menu_app_restaurant;")
# #     restaurants = cursor.fetchall()

# #     restaurant_objects = []
# #     image_downloads = {}

# #     for rest in restaurants:
# #         rest_id, user_id, name, address, telegram, instagram, logo, photo = rest

# #         logging.info(f"🚀 Обработка ресторана: {name}")

# #         admin = UserModel.objects.filter(id=user_id).first()
# #         safe_name = name.replace(" ", "_").lower()

# #         # Пути для logo и photo
# #         logo_folder = f"vendors/{safe_name}/logo"
# #         photo_folder = f"vendors/{safe_name}/backgroud"
# #         logo_filename = "logo.jpg"
# #         photo_filename = "background.jpg"

# #         # Добавляем задачи скачивания в словарь
# #         image_downloads[rest_id] = {
# #             "logo": (logo, logo_folder, logo_filename),
# #             "photo": (photo, photo_folder, photo_filename)
# #         }

# #         restaurant_objects.append(
# #             Restaurant(
# #                 id=rest_id,
# #                 admin=admin, 
# #                 name=name, 
# #                 adress=address, 
# #                 telegram_link=telegram if telegram else "telegram", 
# #                 instagram_link=instagram if instagram else "instagram",
# #                 orders_chat_id=1,
# #                 waiter_chat_id=1,
# #                 stir=1,
# #                 legal_name="abc",
# #                 legal_adress="abc",
# #                 contact_entity="+998911234567",
# #                 contact_support="+998911234567"
# #             )
# #         )

#     # # Массово создаем рестораны
#     # Restaurant.objects.bulk_create(restaurant_objects, ignore_conflicts=True)
#     # logging.info(f"✅ {len(restaurant_objects)} ресторанов успешно добавлено в базу")

#     # # Асинхронно загружаем все изображения
#     # with ThreadPoolExecutor(max_workers=5) as executor:
#     #     results = {
#     #         (rest_id, img_type): executor.submit(download_image, *img_data)
#     #         for rest_id, img_dict in image_downloads.items()
#     #         for img_type, img_data in img_dict.items()
#     #     }

#     # # Массовое обновление логотипов и background
#     # updated_restaurants = []
#     # for (rest_id, img_type), future in results.items():
#     #     img_path = future.result()
#     #     if img_path:
#     #         restaurant = Restaurant.objects.get(id=rest_id)
#     #         with open(os.path.join(BASE_DIR, img_path), "rb") as f:
#     #             django_file = File(f)
#     #             if img_type == "logo":
#     #                 restaurant.logo.save(os.path.basename(img_path), django_file, save=False)
#     #             elif img_type == "photo":
#     #                 restaurant.backgroud_photo.save(os.path.basename(img_path), django_file, save=False)
#     #         updated_restaurants.append(restaurant)

#     # # Используем bulk_update для сохранения всех изображений сразу
#     # if updated_restaurants:
#     #     Restaurant.objects.bulk_update(updated_restaurants, ["logo", "backgroud_photo"])
#     #     logging.info(f"✅ {len(updated_restaurants)} изображений успешно обновлено")




# # @transaction.atomic
# # def migrate_categories():
# #     cursor.execute("SELECT id, restaurant_id, name FROM menu_app_category;")
# #     categories = cursor.fetchall()
# #     cat_items = []
# #     for cat in categories:
# #         cat_id, restaurant_id, name = cat
# #         logging.info(f"🚀 Обработка меню: {name}")
# #         restaurant = Restaurant.objects.filter(id=restaurant_id).first()

# #         cat_items.append(
# #             Category(
# #                 id=cat_id,
# #                 restaurant=restaurant,
# #                 name=name,
# #                 )
# #         )
# #     Category.objects.bulk_create(cat_items, ignore_conflicts=True)
# #     logging.info(f"Категории добавлены")



# import os
# import logging
# import uuid
# import requests
# from django.core.files import File
# from django.conf import settings
# from django.db import transaction
# from concurrent.futures import ThreadPoolExecutor, as_completed


# import os
# import logging
# import uuid
# import requests
# from io import BytesIO
# from django.core.files.base import ContentFile

# def download_image_to_django(instance, url):
#     """Скачивает изображение и сохраняет его через Django FileField."""
#     if not url:
#         return None

#     prefix = "https://aurora-api.uz/media/"
#     full_url = prefix + url

#     try:
#         response = requests.get(full_url, timeout=5)
#         response.raise_for_status()

#         ext = os.path.splitext(url)[1] or ".jpg"  # Получаем расширение файла
#         filename = f"{uuid.uuid4().hex}{ext}"  # Генерируем уникальное имя

#         # Используем ContentFile, чтобы Django мог прочитать файл
#         django_file = ContentFile(response.content)

#         # Django сам сохранит файл в нужную папку
#         instance.photo.save(filename, django_file, save=False)
#         return instance.photo.name  # Возвращаем путь, который Django создал
#     except requests.RequestException as e:
#         logging.error(f"❌ Ошибка загрузки {full_url}: {e}")
#         return None



# @transaction.atomic
# def migrate_menus():
#     """Переносит меню и загружает их фото правильно в Django."""
#     cursor.execute("SELECT id, name, description, price, category_id, restaurant_id, photo FROM menu_app_menu;")
#     menus = cursor.fetchall()

#     menu_ids = {menu[0] for menu in menus}
#     restaurant_ids = {menu[5] for menu in menus}
#     category_ids = {menu[4] for menu in menus}

#     # Загружаем рестораны и категории разом
#     restaurants = Restaurant.objects.in_bulk(restaurant_ids)
#     categories = Category.objects.in_bulk(category_ids)

#     menu_objects = []
#     image_downloads = {}

#     for menu_id, name, description, price, category_id, restaurant_id, photo in menus:
#         logging.info(f"🚀 Обработка меню: {name}")

#         restaurant = restaurants.get(restaurant_id)
#         category = categories.get(category_id)

#         if not restaurant or not category:
#             logging.warning(f"⚠ Пропущено: {name} (нет ресторана или категории)")
#             continue

#         # Создаем объект меню
#         menu = Menu(
#             id=menu_id,
#             name=name,
#             description=description,
#             price=price,
#             category=category,
#             restaurant=restaurant,
#         )
#         menu_objects.append(menu)

#         # Готовим задачу загрузки фото
#         if photo:
#             image_downloads[menu_id] = (menu, photo)

#     # Массово создаем меню (без фото)
#     Menu.objects.bulk_create(menu_objects, ignore_conflicts=True)
#     logging.info(f"✅ {len(menu_objects)} блюд успешно добавлено в базу")

#     # Асинхронно загружаем фото
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         future_to_menu = {
#             executor.submit(download_image_to_django, menu, photo): menu
#             for menu, photo in image_downloads.values()
#         }

#         updated_menus = []
#         for future in as_completed(future_to_menu):
#             menu = future_to_menu[future]
#             img_path = future.result()
#             if img_path:
#                 updated_menus.append(menu)

#     # Массово обновляем фото
#     if updated_menus:
#         Menu.objects.bulk_update(updated_menus, ["photo"])
#         logging.info(f"✅ {len(updated_menus)} фото меню успешно обновлено")




# def reset_sequences():
#     print("———————————————————")
#     print("Сброс id для Django")
#     print("———————————————————")
#     with connection.cursor() as cursor:
#         tables = ["restaurant_restaurant", "product_category", "authentication_usermodel", "product_menu"]
#         for table in tables:
#             cursor.execute(
#                 f"SELECT setval(pg_get_serial_sequence('{table}', 'id'), "
#                 f"COALESCE((SELECT MAX(id) FROM {table}), 1) + 1, false);"
#             )


# def run_migrations():
#     # migrate_users()
#     # migrate_restaurants()
#     # migrate_categories()
#     migrate_menus()
#     reset_sequences()
#     print("****POLNIY USPEX*****")


# if __name__ == "__main__":
#     run_migrations()








# # @transaction.atomic
# # def migrate_restaurants():
# #     cursor.execute("SELECT id, user_id, name, adress, telegram, instagramm FROM menu_app_restaurant;")
# #     restaurants = cursor.fetchall()

# #     for rest in restaurants:
# #         rest_id, user_id, name, address, telegram, instagram = rest
# #         print(f"———————————————————")
# #         print(f"Процесс для: ——> {name}")
# #         print(f"———————————————————")
# #         admin = UserModel.objects.filter(id=user_id).first()  # Связываем с новым пользователем

# #         Restaurant.objects.create(
# #             id=rest_id,
# #             admin=admin, 
# #             name=name, 
# #             adress=address, 
# #             telegram_link="telegram", 
# #             instagram_link="instagram",
# #             backgroud_photo="1.jpg",
# #             logo="1.jpg",
# #             orders_chat_id=1,
# #             waiter_chat_id=1,
# #             stir=1,
# #             legal_name="abc",
# #             legal_adress="abc",
# #             contact_entity="+998911234567",
# #             contact_support="+998911234567"

# #         )

# #     print("————————————————")
# #     print("Restaurant uspex")
# #     print("————————————————")
