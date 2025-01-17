# Generated by Django 4.0.6 on 2023-02-20 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0040_feedlinks_created_at_feedlinks_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawlerkeyword',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crawlerkeyword',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
