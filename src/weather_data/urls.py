from django.urls import path

from weather_data.views import WeatherView, StatsView


urlpatterns = [
    path("weather/", WeatherView.as_view(), name="weather_data"),
    path("weather/stats", StatsView.as_view(), name="stats"),
]
