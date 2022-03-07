from .models import Category, Tag, Color, Image
from rest_framework import generics, pagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializers, TagSerializers, ColorSerializer, ImageSerializer
from .filters import ImageFilter
from django_filters import rest_framework as filters


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 5


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class ColorListAPIView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ImageListAPIView(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backend = (filters.DjangoFilterBackend)
    filterset_class = ImageFilter
    pagination_class = StandardResultsSetPagination


class ImageCountAPIView(APIView):
    def get(self, request):
        image_count = Image.objects.all().count()
        return Response({"count": image_count})
