# Generated by Django 4.0.6 on 2023-04-20 11:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectaccountanalysis',
            name='country_dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AddField(
            model_name='projectaccountanalysis',
            name='language_dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AddField(
            model_name='projectaccountanalysis',
            name='sentiment_dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AddField(
            model_name='projectaccountanalysis',
            name='source_dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
        migrations.AddField(
            model_name='projectaccountanalysis',
            name='source_filter',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=None, null=True, size=None),
        ),
    ]
