# Generated by Django 4.0.6 on 2023-02-23 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0041_crawlerkeyword_created_at_crawlerkeyword_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlerOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='Saudi Arabia', max_length=50)),
                ('tbm', models.CharField(choices=[('isch', 'Google Images API'), ('lcl', 'Google Local API'), ('vid', 'Google Videos API'), ('nws', 'Google News API'), ('shop', 'Google Shopping API')], default='nws', max_length=5)),
                ('gl', models.CharField(default='sa', max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]