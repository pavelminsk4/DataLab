# Generated by Django 4.0.6 on 2023-01-12 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0033_feedlinks_tier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]
