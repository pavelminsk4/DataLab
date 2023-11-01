# Generated by Django 4.0.6 on 2023-10-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_profile_platform_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, choices=[('admin', 'Admin'), ('company', 'Company'), ('regular_user', 'Regular User'), ('picker', 'Picker'), ('writer', 'Writer'), ('publisher', 'Publisher')], default='Company', max_length=30, null=True),
        ),
    ]