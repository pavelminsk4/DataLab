# Generated by Django 4.0.6 on 2023-01-09 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0032_alter_feedlinks_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedlinks',
            name='tier',
            field=models.IntegerField(default=0),
        ),
    ]
