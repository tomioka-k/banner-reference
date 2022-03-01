# Generated by Django 4.0.3 on 2022-03-01 15:00

import banner.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_type', models.CharField(choices=[('vertical', 'Vertical'), ('horizontal', 'horizontal'), ('square', 'square')], max_length=20)),
                ('image', models.ImageField(upload_to=banner.models.image_path)),
                ('width', models.IntegerField()),
                ('heigit', models.IntegerField()),
                ('release_date', models.DateField()),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='banner.tag')),
            ],
        ),
    ]
