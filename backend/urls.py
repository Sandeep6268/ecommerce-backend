
from django.contrib import admin
from django.urls import path,include
from .views import hello_world
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/csrf/", get_csrf_token),
    path('', include('products.urls')),
    path('', include('cart.urls')),
    path('api/', include('users.urls')),
     # Djoser endpoints for user management
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
