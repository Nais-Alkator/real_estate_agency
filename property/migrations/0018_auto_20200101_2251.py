
# Generated by Django 2.2.4 on 2020-01-01 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20191216_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complainer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intruders', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='intruder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complainers', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
    ]

