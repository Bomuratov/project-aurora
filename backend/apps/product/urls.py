from rest_framework import routers
from apps.product.views.menu_view import MenuView
from apps.product.views.category_view import CategoryView


router = routers.DefaultRouter()

router.register(r"menu", MenuView, basename="menu")
router.register(r"category", CategoryView, basename="category")

urlpatterns = router.urls