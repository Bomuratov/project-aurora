from rest_framework.routers import DefaultRouter
from users.views.user_view import UserView


router = DefaultRouter()


router.register(r"auth", UserView, basename="auth")
