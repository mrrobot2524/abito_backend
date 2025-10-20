from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import ItemViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'product', ItemViewSet, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# В режиме разработки: отдаём медиа-файлы
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
