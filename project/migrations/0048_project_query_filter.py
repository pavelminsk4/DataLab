# Generated by Django 4.0.6 on 2023-04-13 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0047_alter_project_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='query_filter',
            field=models.CharField(max_length=300, null=True),
        ),
    ]