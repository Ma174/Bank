# Generated by Django 3.0.2 on 2020-01-04 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200105_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='age',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='claim',
            name='wage',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
