import django_filters
from apps.surveys.models import Survey, Section


class SurveyFilter(django_filters.FilterSet):
    start_date_from = django_filters.DateFilter(field_name="start_date", lookup_expr="gte")
    start_date_to = django_filters.DateFilter(field_name="start_date", lookup_expr="lte")
    start_date_on = django_filters.DateFilter(field_name="start_date", lookup_expr="exact")
    end_date_from = django_filters.DateFilter(field_name="end_date", lookup_expr="gte")
    end_date_to = django_filters.DateFilter(field_name="end_date", lookup_expr="lte")
    end_date_on = django_filters.DateFilter(field_name="end_date", lookup_expr="exact")

    class Meta:
        model = Survey
        fields = ["created_by", "start_date_from", "start_date_to", "start_date_on",
                  "end_date_from", "end_date_to", "end_date_on"]


class SectionFilter(django_filters.FilterSet):
    class Meta:
        model = Section
        fields = ["survey"]
