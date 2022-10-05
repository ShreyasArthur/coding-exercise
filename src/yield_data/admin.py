from django.contrib.admin import register, ModelAdmin

from yield_data.models import YieldData


@register(YieldData)
class YieldDataAdmin(ModelAdmin):
    list_display = ["year", "US_corn_grain_yield"]
    list_filter = [
        "year",
    ]
    ordering = [
        "year",
    ]
