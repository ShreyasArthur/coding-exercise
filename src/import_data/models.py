'''import_data BaseModel'''
from django.db import models


class BaseModel(models.Model):
    """
    created_at and update_at timestamps.
    """
    created_at = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(
        auto_now=True, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        """
        model will be an abstract base class.
        """
        abstract = True
