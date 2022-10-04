from rest_framework.viewsets import ModelViewSet
from .models import ProductModel,CategoryModel
from .serializers import ProductSerializer,CategorySerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

