from rest_framework.viewsets import ModelViewSet
from products.models import ProductModel,CategoryModel
from products.serializers import ProductSerializer,CategorySerializer
from .permissions import IsOwnerOrReadOnly,OnlyOwner
from user.models import UserModel
from user.serializers import UserSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [OnlyOwner]


