# Generated by Django 4.0.3 on 2022-03-01 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_alter_image_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='heigit',
            new_name='height',
        ),
    ]
