from django.db import models
from bulk_update_or_create import BulkUpdateOrCreateQuerySet


from import_data.models import BaseModel


class YieldData(BaseModel):
    """
    YieldData model is used to store crop yield data
    """

    year = models.PositiveSmallIntegerField(unique=True)
    US_corn_grain_yield = models.IntegerField()

    objects = BulkUpdateOrCreateQuerySet.as_manager()
