# Generated by Django 4.0.6 on 2023-04-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_social', '0015_socialwidgetslist_authors_by_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsocial',
            name='source',
            field=models.CharField(blank=True, default='Social', max_length=100, null=True),
        ),
    ]
