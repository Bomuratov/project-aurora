from rest_framework.routers import DefaultRouter
from apps.authentication.views.user_register_view import UserView
from authentication.views.user_login import UserLoginView
from authentication.views.vendor_login import VendorLoginView


router = DefaultRouter()


router.register(r"auth/register", UserView, basename="register")
# router.register(r"auth/register", UserView, basename="register")
