from restaurant.routers.vendor_router import router as vendor_router
from apps.authentication.routers.router import router as auth_router


urlpatterns = vendor_router.urls
urlpatterns = auth_router.urls