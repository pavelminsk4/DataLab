# Generated by Django 4.0.6 on 2022-10-20 08:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_search_date',
            field=models.DateTimeField(default="2021-10-16T00:00:00Z"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='start_search_date',
            field=models.DateTimeField(default="2021-10-10T00:00:00Z"),
            preserve_default=False,
        ),
    ]
