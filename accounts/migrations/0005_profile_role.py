# Generated by Django 4.0.6 on 2022-12-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_department_description_department_logo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('company', 'Company'), ('regular_user', 'Regular User'), ('picker', 'Picker'), ('writer', 'Writer'), ('publisher', 'Publisher')], max_length=30, null=True),
        ),
    ]