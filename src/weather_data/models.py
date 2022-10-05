from django.db import models

from import_data.missing_value import MISSING_VALUE
from import_data.models import BaseModel


class WeatherData(BaseModel):
    """
    Used to store data from weather stations.
    """

    station_id = models.CharField(max_length=50)
    date = models.DateField()
    max_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    min_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    precipitation = models.FloatField(
        default=MISSING_VALUE,
    )

    class Meta:
        unique_together = [
            "station_id",
            "date",
        ]


class Statistics(BaseModel):
    """
    Used to store the stats of WeatherData .
    """

    station_id = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    avg_max_temp = models.FloatField(
        null=True,
    )
    avg_min_temp = models.FloatField(
        null=True,
    )
    total_precipitation = models.FloatField(
        null=True,
    )

    class Meta:
        unique_together = [
            "station_id",
            "year",
        ]
