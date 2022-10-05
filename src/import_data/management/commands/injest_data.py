'''injesting the yeild and weather data'''
import os
import pandas as pd

from django.core.management.base import BaseCommand

from yield_data.models import YieldData
from weather_data.models import WeatherData

WEATHER = "weather_data"
YIELD = "yield_data"


class Command(BaseCommand):
    """
    Django take Command-line arguments and handle
    """

    def __init__(self):
        self.success_count = 0
        self.fail_count = 0
        super().__init__()

    def add_arguments(self, parser):
        parser.add_argument(
            "-w",
            "--weather_data",
            action="store_true",
        )
        parser.add_argument(
            "-y",
            "--yield_data",
            action="store_true",
        )

    def handle(self, *args, **kwargs):
        path = "../{}/"
        if kwargs.get(WEATHER, False):
            path = path.format("wx_data")
            self.read_files(path, WEATHER)
        elif kwargs.get(YIELD, False):
            path = path.format("yld_data")
            self.read_files(path, YIELD)
        else:
            self.stdout.write(
                "Command Failed. Please verify the arguments and try again!")

    def read_files(self, path: str, data_type: str) -> None:
        """
        reads the files from wx_data and yld_data
        """
        files = os.listdir(path)
        for file in files:
            if file.endswith(".txt"):
                file_name = file[:-4]
                file_path = path + file
                if data_type == WEATHER:
                    self.load_weather_data(file_path, file_name)
                else:
                    self.load_yield_data(file_path)
                self.stdout.write(f"Injesting file: {file}")

    def load_weather_data(self, file_path, file_name):
        """
        Using the Django ORM's Bulk_create since it makes it easier by combining all creates into 1
        """
        df = pd.read_table(
            file_path,
            header=None,
            names=["date", "max_temp", "min_temp", "precipitation"],
        )
        df["station_id"] = file_name
        df["date"] = df["date"].apply(self.date_format)
        df["max_temp"] = df["max_temp"].apply(self.shift_decimal_by_one)
        df["min_temp"] = df["min_temp"].apply(self.shift_decimal_by_one)
        df["precipitation"] = df["precipitation"].apply(
            self.shift_decimal_by_two)
        records = df.to_dict("records")
        objs = [WeatherData(**record) for record in records]
        WeatherData.objects.bulk_create(objs, ignore_conflicts=True)

    def load_yield_data(self, file_path):
        """
        Will load yield data for that year.
        """
        df = pd.read_table(
            file_path,
            header=None,
            names=["year", "US_corn_grain_yield"],
        )
        records = df.to_dict("records")
        objs = [YieldData(**record) for record in records]
        returned_objs = YieldData.objects.bulk_update_or_create(
            objs, ["US_corn_grain_yield"], match_field="year", yield_objects=True
        )
        returned_objs = list(returned_objs)

    def date_format(self, date: str) -> str:
        """
        Changes date format to Django compatibe
        """
        date = str(date)
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        formatted_date = f"{year}-{month}-{day}"
        return formatted_date

    def shift_decimal_by_one(self, num: float) -> float:
        """
        Shifts decimal by one
        """
        shifted_num = self.shift_decimal(num, -1)
        return round(shifted_num, 1)

    def shift_decimal_by_two(self, num: float) -> float:
        """
        Shifts decimal by two
        """
        shifted_num = self.shift_decimal(num, -2)
        return round(shifted_num, 2)

    def shift_decimal(self, num: float, shift: int) -> float:
        """
        This is if the number is not the float representation of a MISSING_VALUE
        """
        if num == -9999.0:
            return num
        shifted_num = num * 10.0**shift
        return shifted_num
