from rest_framework.viewsets import ModelViewSet
from .models import ProductModel,CategoryModel
from .serializers import ProductSerializer,CategorySerializer
from .permissions import IsOwnerOrReadOnly,IsSuperUserPermission,UserProfilePermissions
from rest_framework import permissions

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]

