# Generated by Django 5.1 on 2024-09-01 07:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteinfo', '0004_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='map_url',
        ),
        migrations.AddField(
            model_name='location',
            name='iframe_code',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
