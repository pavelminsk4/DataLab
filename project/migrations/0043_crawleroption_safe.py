# Generated by Django 4.0.6 on 2023-02-24 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0042_crawleroption'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawleroption',
            name='safe',
            field=models.CharField(choices=[('active', 'Filtering for adult content - Active'), ('off', 'Filtering for adult content - Off')], default='active', max_length=10),
        ),
    ]
