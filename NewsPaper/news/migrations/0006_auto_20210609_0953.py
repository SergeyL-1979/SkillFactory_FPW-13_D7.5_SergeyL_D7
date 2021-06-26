# Generated by Django 3.2.2 on 2021-06-09 06:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0005_auto_20210608_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_subscriber',
        ),
        migrations.AddField(
            model_name='category',
            name='subscriber',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
