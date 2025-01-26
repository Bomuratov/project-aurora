from restaurant.routers.vendor_router import router as vendor_router
from users.routers.user_router import router as auth_router


urlpatterns = vendor_router.urls
urlpatterns = auth_router.urls