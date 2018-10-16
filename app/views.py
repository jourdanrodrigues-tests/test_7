from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from app.filters import IsOrderOwner
from app.models import Order
from app.serializers import OrderSerializer


class OrderViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (IsOrderOwner,)
    permission_classes = (IsAuthenticated,)
