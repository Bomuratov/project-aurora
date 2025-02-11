from rest_framework.routers import DefaultRouter
from apps.restaurant.views.restaurant_view import RestaurantView

router = DefaultRouter()

router.register(r"restaurant", RestaurantView, basename="restaurant")

urlpatterns = router.urls