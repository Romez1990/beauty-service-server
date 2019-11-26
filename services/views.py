from rest_framework.generics import ListAPIView

from .models import ServiceGroup
from .serializer import ServiceGroupDetailSerializer


class ServiceGroupsListView(ListAPIView):
    serializer_class = ServiceGroupDetailSerializer
    queryset = ServiceGroup.objects.all()
