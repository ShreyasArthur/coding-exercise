# importing
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from yield_data.yield_filter import YieldFilter
from yield_data.models import YieldData
from yield_data.serializers import YieldSerializer


class YieldsView(ListAPIView):
    queryset = YieldData.objects.all()
    serializer_class = YieldSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = YieldFilter
