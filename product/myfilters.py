from .models import Product
from  django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'brand': ['exact'],
            'price': ['lte','gte','range'],
        }