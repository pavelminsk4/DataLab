# Generated by Django 4.0.6 on 2023-11-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0077_project_synched_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='resume_offset',
            field=models.CharField(blank=True, default='earliest', max_length=20, null=True),
        ),
    ]
