# Generated by Django 4.0.6 on 2023-07-27 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0053_changingonlinesentiment_delete_changingsentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='query_filter',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]