# Generated by Django 4.0.6 on 2023-09-20 12:03

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('tweet_binder', '0012_livereport_livesearchproject_end_date_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='tweetbinderpost',
            index=models.Index(fields=['date'], name='tweet_binde_date_42834a_idx'),
        ),
        migrations.AddIndex(
            model_name='tweetbinderpost',
            index=django.contrib.postgres.indexes.GinIndex(django.contrib.postgres.indexes.OpClass(django.db.models.functions.text.Upper('text'), name='gin_trgm_ops'), name='tb_text_gin_index'),
        ),
        migrations.AddIndex(
            model_name='tweetbinderpost',
            index=django.contrib.postgres.indexes.GinIndex(django.contrib.postgres.indexes.OpClass(django.db.models.functions.text.Upper('user_name'), name='gin_trgm_ops'), name='tb_user_name_gin_index'),
        ),
        migrations.AddIndex(
            model_name='tweetbinderpost',
            index=django.contrib.postgres.indexes.GinIndex(django.contrib.postgres.indexes.OpClass(django.db.models.functions.text.Upper('user_alias'), name='gin_trgm_ops'), name='tb_user_alias_gin_index'),
        ),
    ]
