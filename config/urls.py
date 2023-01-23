from django.contrib import admin
from django.urls import path, include
from .views import home

from django.conf import settings
from django.conf.urls.static import static
from marketplace.views import cart, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('', include('accounts.urls')),
    path('marketplace/', include('marketplace.urls')),
    # Cart
    path('cart/', cart, name='cart'),
    # Search
    path('search/', search, name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)