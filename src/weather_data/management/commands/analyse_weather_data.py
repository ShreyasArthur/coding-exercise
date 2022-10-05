"""analyse weather data"""
from django.core.management.base import BaseCommand

from weather_data.utils import generate_all_years, calculate_stats


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        """analyse weather data"""
        years = generate_all_years()

        if years:
            self.stdout.write(
                "Started analysing the weather data. Please wait!")
            calculate_stats(years)
            self.stdout.write("Finished analysis of weather data")
        else:
            self.stdout.write("No weather data to analyze")
