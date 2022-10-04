from rest_framework.viewsets import ModelViewSet
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
