# Generated by Django 2.2.4 on 2019-12-01 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20191130_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(verbose_name='Новостройка'),
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intruder', models.IntegerField(db_index=True, verbose_name='Квартира, на которую пожаловались')),
                ('text', models.TextField(blank=True, verbose_name='Текст жалобы')),
                ('complainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat')),
            ],
        ),
    ]
