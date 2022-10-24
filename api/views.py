from rest_framework.viewsets import ModelViewSet
from products.models import ProductModel,CategoryModel
from products.serializers import ProductSerializer,CategorySerializer
from .permissions import IsOwnerOrReadOnly


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

