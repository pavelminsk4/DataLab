# Generated by Django 4.0.6 on 2023-12-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_binder', '0016_alter_tweetbinderpost_creation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetbinderpost',
            name='country',
            field=models.CharField(blank=True, default='USA', max_length=200, null=True, verbose_name='country'),
        ),
    ]
