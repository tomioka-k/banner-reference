from django.db import models
import uuid
from django.core.validators import MinLengthValidator
from PIL import Image as PIL_Image


def image_path(instance, filename):
    return 'image/{}.{}'.format(uuid.uuid4(), filename.split('.')[-1])


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20, unique=True)
    code = models.CharField(
        verbose_name='color code',
        unique=True, max_length=6,
        validators=[MinLengthValidator(6)],
        help_text='6 digits'
    )

    def __str__(self):
        return f'{self.name}_(#{self.code})'


class Image(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    image_type = models.CharField(
        choices=(
            ('vertical', 'Vertical'),
            ('horizontal', 'horizontal'),
            ('square', 'square')
        ),
        max_length=20
    )
    image = models.ImageField(upload_to=image_path)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    release_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.image.url

    def save(self, *args, **kwargs):
        im = PIL_Image.open(self.image)
        self.width = im.width
        self.height = im.height
        if im.width == im.height:
            self.image_type = 'square'
        elif im.width > im.height:
            self.image_type = 'horizontal'
        else:
            self.image_type = 'vertical'
        super().save(*args, **kwargs)
