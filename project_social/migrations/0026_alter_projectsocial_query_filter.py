# Generated by Django 4.0.6 on 2023-11-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0025_socialwidgetslist_gender_by_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectsocial',
            name='query_filter',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
