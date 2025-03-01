from rest_framework import routers
from promo.views.promo_view import PromoView


router = routers.SimpleRouter()

router.register(r"promo", PromoView, basename="menu")


urlpatterns = router.urls