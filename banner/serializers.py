from dataclasses import field, fields
from .models import Category, Tag, Color, Image
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name', 'code')


class ImageSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    color = ColorSerializer()
    tag = TagSerializers(many=True)

    class Meta:
        model = Image
        fields = ('id', 'category', 'tag', 'image_type', 'image', 'color',
                  'width', 'height', 'release_date')
