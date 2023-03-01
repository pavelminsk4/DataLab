# Generated by Django 4.0.6 on 2023-03-01 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_department_current_number_of_projects_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='current_number_of_social_projects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='department',
            name='max_projects_social',
            field=models.IntegerField(default=1),
        ),
    ]
