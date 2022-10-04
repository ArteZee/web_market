from rest_framework.viewsets import ModelViewSet
from .models import OrderModel
from .serializers import OrderSerializer

class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()

