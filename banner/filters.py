from django_filters import rest_framework as filters
from .models import Image


class ImageFilter(filters.FilterSet):
    class Meta:
        model = Image
        fields = ['category', 'tag', 'image_type', 'color', 'width', 'height']
