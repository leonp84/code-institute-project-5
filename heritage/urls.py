from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('my_account/', include('my_account.urls')),
    path('accounts/', include('allauth.urls')),
    path('product/', include('product.urls')),
    path('checkout/', include('checkout.urls')),
]

# Setting to serve Django Media files in Development environment

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
