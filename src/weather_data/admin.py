from django.contrib.admin import register, ModelAdmin

from weather_data.models import WeatherData, Statistics
from weather_data.utils import generate_all_years, calculate_stats


@register(WeatherData)
class WeatherDataAdmin(ModelAdmin):
    list_display = [
        "station_id",
        "date",
        "max_temp",
        "min_temp",
        "precipitation",
    ]
    list_filter = ["date"]
    ordering = ["date"]
    actions = [
        "calculate_all_statistics",
    ]

    def calculate_all_statistics(self):
        years = generate_all_years()
        if years:
            calculate_stats(years)
        return


@register(Statistics)
class StatisticsAdmin(ModelAdmin):
    list_display = [
        "station_id",
        "year",
        "avg_max_temp",
        "avg_min_temp",
        "total_precipitation",
    ]
    list_filter = ["station_id", "year"]
    ordering = ["station_id", "year"]
