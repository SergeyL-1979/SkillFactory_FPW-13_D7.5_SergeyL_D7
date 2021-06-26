# Generated by Django 3.2.2 on 2021-05-31 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210516_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.utcnow)),
                ('client_name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Категория'),
        ),
    ]
