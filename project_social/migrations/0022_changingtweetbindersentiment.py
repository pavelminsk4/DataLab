# Generated by Django 4.0.6 on 2023-06-09 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_department_current_number_of_account_analysis_projects_and_more'),
        ('tweet_binder', '0011_tweetbinderpost_imp_sentiment'),
        ('project_social', '0021_projectsocial_expert_mode_projectsocial_query_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangingTweetbinderSentiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentiment', models.CharField(max_length=10, verbose_name='sentiment')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.department')),
                ('tweet_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet_binder.tweetbinderpost')),
            ],
        ),
    ]
