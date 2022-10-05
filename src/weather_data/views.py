from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from weather_data.filters import WeatherFilter, StatisticsFilter
from weather_data.models import WeatherData, Statistics
from weather_data.serializers import WeatherDataSerializer, StatisticsSerializer


class WeatherView(ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = WeatherFilter


class StatsView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = StatisticsFilter
