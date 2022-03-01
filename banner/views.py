from .models import Category, Tag, Color, Image
from rest_framework import generics
from .serializers import CategorySerializers, TagSerializers, ColorSerializer, ImageSerializer


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
