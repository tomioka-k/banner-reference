from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Color, Tag, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Color)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', 'code')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):

    list_display = ('_format_image', 'category', '_tags',
                    'image_type', 'width', 'height', 'release_date', )
    list_filter = ('image_type', 'category', 'tag', 'color')
    autocomplete_fields = ('category', 'tag', 'color')
    readonly_fields = ('image_type', 'width', 'height', 'release_date')

    def _format_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="360"/>', obj.image.url)

    _format_image.short_description = "Image"
    _format_image.empty_value_display = 'No Image'

    def _tags(self, row):
        return ' , '.join([x.name for x in row.tag.all()])
