from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from productos.views import ProductoViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"productos", ProductoViewSet)


def health(request):
    return JsonResponse({"status": "UP"})


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/health", health),
    path("api/", include(router.urls)),
]
