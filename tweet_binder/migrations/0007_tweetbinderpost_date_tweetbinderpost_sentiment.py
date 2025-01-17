# Generated by Django 4.0.6 on 2023-03-21 14:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_binder', '0006_tweetbinderpost_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetbinderpost',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tweetbinderpost',
            name='sentiment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
