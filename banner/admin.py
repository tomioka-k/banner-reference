from django.contrib import admin
from .models import Category, Color, Tag, Image

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Color)
# admin.site.register(Image)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('image_type', 'width', 'height', 'release_date')
