# Generated by Django 4.0.6 on 2023-05-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_binder', '0010_tweetbinderusertracker_account_analysis_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetbinderpost',
            name='imp_sentiment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
