# Generated by Django 4.0.6 on 2023-04-13 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_analysis', '0001_initial'),
        ('tweet_binder', '0009_tweetbinderusertracker_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweetbinderusertracker',
            name='account_analysis_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account_analysis.projectaccountanalysis'),
        ),
    ]
