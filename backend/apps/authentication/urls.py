from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.authentication.views.user_register_view import UserView
from authentication.views.user_login import UserLoginView
from authentication.views.vendor_login import VendorLoginView


router = DefaultRouter()

# router.register(r"register", UserView, basename="register")

urlpatterns = [
    path("register", UserView.as_view({"post": "create"}), name="user-register"),
    path("user/", UserView.as_view({"get": "list"}), name="user-get-list"),
    path("user/me", UserView.as_view({"get": "retrieve"}), name="user-me"),
    path("user/<int:pk>", UserView.as_view({"get": "retrieve"}), name="user-get"),
    path("user/<int:pk>", UserView.as_view({"put": "update"}), name="user-update"),
    path("user/<int:pk>", UserView.as_view({"delete": "destroy"}), name="user-delete"),
    path(
        "user/<int:pk>/verify",
        UserView.as_view({"patch": "verification"}),
        name="user-verify",
    ),
    path(
        "user/<int:pk>/regenerate",
        UserView.as_view({"patch": "generate"}),
        name="user-generate",
    ),
    path("user/login", UserLoginView.as_view(), name="user-login"),
    path("vendor/login", VendorLoginView.as_view(), name="vendor-login"),
]

# router.register(r"vendor/login", UserLoginView.as_view(), basename="vendor-login")
# router.register(r"user/login", VendorLoginView.as_view(), basename="user-login")


# urlpatterns += router.urls


