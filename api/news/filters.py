import django_filters
from rest_framework import filters

class NewsFilter(filters.FilterSet):
    timestamp_gte = django_filters.DateTimeFilter(name="date_joined", lookup_expr='gte')
    class Meta:
        model = Event
        fields = ['tags', 'date_joined', 'date_joined_gte']
