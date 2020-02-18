# Generated by Django 3.0.dev20190703113551 on 2020-01-31 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_auto_20200131_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='age',
            field=models.CharField(help_text='Укажите Ваш возраст', max_length=2),
        ),
        migrations.AlterField(
            model_name='claim',
            name='aim',
            field=models.CharField(help_text='Введите цель получения кредита/займа', max_length=100),
        ),
        migrations.AlterField(
            model_name='claim',
            name='mail',
            field=models.EmailField(help_text='Введите Ваш email', max_length=254),
        ),
        migrations.AlterField(
            model_name='claim',
            name='name',
            field=models.CharField(help_text='Введите Ваше имя', max_length=20),
        ),
        migrations.AlterField(
            model_name='claim',
            name='surname',
            field=models.CharField(help_text='Введите Вашу фамилию', max_length=20),
        ),
        migrations.AlterField(
            model_name='claim',
            name='wage',
            field=models.CharField(help_text='Укажите размер Вашей з/п', max_length=50),
        ),
        migrations.AlterField(
            model_name='claim',
            name='work',
            field=models.CharField(help_text='Место Вашей работы', max_length=100),
        ),
    ]