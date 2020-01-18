# Generated by Django 2.2.4 on 2020-01-18 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0018_auto_20200101_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainers', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='intruder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intruders', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]