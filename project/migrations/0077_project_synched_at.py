# Generated by Django 4.0.6 on 2023-11-21 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0076_project_expert_presets'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='synched_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
