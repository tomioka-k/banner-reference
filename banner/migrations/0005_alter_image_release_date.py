# Generated by Django 4.0.3 on 2022-03-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0004_rename_heigit_image_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='release_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
