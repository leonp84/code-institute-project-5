from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('my_account/', include('my_account.urls')),
    path('accounts/', include('allauth.urls')),
    path('product/', include('product.urls')),
    path('checkout/', include('checkout.urls')),
    # Make robots.txt accessible as root file
    path('robots.txt', TemplateView.as_view(template_name="robots.txt",
                                            content_type="text/plain")),
    # Make sitemaps.xml accessible as root file
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml",
                                             content_type="text/xml")),
]

# Setting to serve Django Media files in Development environment

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)