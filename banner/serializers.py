from dataclasses import field, fields
from .models import Category, Tag, Color, Image
from rest_framework import serializers


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('name', 'code')


class ImageSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    color = ColorSerializer()
    tag = serializers.StringRelatedField(many=True)

    class Meta:
        model = Image
        fields = ('category', 'tag', 'image_type', 'image', 'color',
                  'width', 'height', 'release_date')
