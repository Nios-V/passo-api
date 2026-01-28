import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    min_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    max_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')
    title = django_filters.CharFilter(field_name="title", lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['min_date', 'max_date', 'title', 'location']