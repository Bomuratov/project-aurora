from rest_framework.routers import DefaultRouter
from vendor.views.vendor_view import VendorView

router = DefaultRouter()

router.register(r"vendor", VendorView, basename="vendor")