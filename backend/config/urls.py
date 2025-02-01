from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.authentication.views.user_login import UserLoginView
from apps.authentication.views.vendor_login import VendorLoginView
# from apps.auth.views.user_token import UserTokenObtainView
# from apps.vendors.views.vendor_token import VendorTokenObtainView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("apps.urls")),
    path('user/token/', UserLoginView.as_view(), name='user_token_obtain_pair'),
    path('vendor/token/', VendorLoginView.as_view(), name='vendor_token_obtain_pair'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)