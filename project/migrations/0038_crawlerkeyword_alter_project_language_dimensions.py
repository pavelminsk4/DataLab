# Generated by Django 4.0.6 on 2023-02-07 14:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0037_newfeedlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlerKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, verbose_name='Word')),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='language_dimensions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None),
        ),
    ]
