from rest_framework import serializers

from yield_data.models import YieldData


class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = YieldData
        fields = ["year", "US_corn_grain_yield", "created_at", "updated_at"]
