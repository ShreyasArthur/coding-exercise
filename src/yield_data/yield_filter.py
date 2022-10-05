from django_filters import FilterSet, CharFilter

from yield_data.models import YieldData


class YieldFilter(FilterSet):
    year = CharFilter(field_name="year", lookup_expr="iexact")

    class Meta:
        model = YieldData
        fields = ["year"]
