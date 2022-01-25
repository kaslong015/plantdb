import django_filters

from .models import *

class PlantFilter(django_filters.FilterSet):
    class Meta:
        model = Plant
        fields = ['name']
