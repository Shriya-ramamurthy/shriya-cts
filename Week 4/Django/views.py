from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# ModelViewSet automatically handles Create, Read, Update, and Delete actions
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
