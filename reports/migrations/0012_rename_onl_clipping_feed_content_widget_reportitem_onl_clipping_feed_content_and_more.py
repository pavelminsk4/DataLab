# Generated by Django 4.0.6 on 2023-05-04 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_alter_regularreport_items_alter_regularreport_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_clipping_feed_content_widget',
            new_name='onl_clipping_feed_content',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_content_volume_top_5_authors_widget',
            new_name='onl_content_volume_top_authors',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_content_volume_top_5_countries_widget',
            new_name='onl_content_volume_top_countries',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_content_volume_top_5_source_widget',
            new_name='onl_content_volume_top_source',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_sentiment_for_period_widget',
            new_name='onl_sentiment_for_period',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_sentiment_top_10_authors_widget',
            new_name='onl_sentiment_top_authors',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_sentiment_top_10_countries_widget',
            new_name='onl_sentiment_top_countries',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_sentiment_top_10_languages_widget',
            new_name='onl_sentiment_top_languages',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_sentiment_top_10_sources_widget',
            new_name='onl_sentiment_top_sources',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_summary_widget',
            new_name='onl_summary',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_top_10_authors_by_volume_widget',
            new_name='onl_top_authors_by_volume',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_top_10_brands_widget',
            new_name='onl_top_brands',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_top_10_countries_widget',
            new_name='onl_top_countries',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_top_10_languages_widget',
            new_name='onl_top_languages',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='onl_volume_widget',
            new_name='onl_volume',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='soc_content_volume_by_top_authors',
            new_name='soc_content_volume_top_authors',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='soc_content_volume_by_top_languages',
            new_name='soc_content_volume_top_languages',
        ),
        migrations.RenameField(
            model_name='reportitem',
            old_name='soc_content_volume_by_top_locations',
            new_name='soc_content_volume_top_locations',
        ),
    ]
