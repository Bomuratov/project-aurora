from rest_framework.routers import DefaultRouter
from restaurant.views.vendor_view import VendorView

router = DefaultRouter()

router.register(r"vendor", VendorView, basename="vendor")