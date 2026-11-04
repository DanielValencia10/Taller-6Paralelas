from rest_framework import viewsets

from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    """CRUD completo: listar, crear, traer, actualizar y borrar productos."""

    queryset = Producto.objects.all().order_by("id")
    serializer_class = ProductoSerializer
    http_method_names = ["get", "post", "put", "delete", "head", "options"]
