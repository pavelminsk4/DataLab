# Generated by Django 4.0.6 on 2023-05-11 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0039_widgetslist2_authors_by_language_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='clipping_feed_content_widget',
            new_name='clipping_feed_content',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='content_volume_top_5_authors_widget',
            new_name='content_volume_top_authors',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='content_volume_top_5_countries_widget',
            new_name='content_volume_top_countries',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='content_volume_top_5_source_widget',
            new_name='content_volume_top_sources',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='sentiment_for_period_widget',
            new_name='sentiment_for_period',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='sentiment_top_10_authors_widget',
            new_name='sentiment_top_authors',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='sentiment_top_10_countries_widget',
            new_name='sentiment_top_countries',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='sentiment_top_10_languages_widget',
            new_name='sentiment_top_languages',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='sentiment_top_10_sources_widget',
            new_name='sentiment_top_sources',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='summary_widget',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='top_10_authors_by_volume_widget',
            new_name='top_authors',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='top_10_brands_widget',
            new_name='top_brands',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='top_10_countries_widget',
            new_name='top_countries',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='top_10_languages_widget',
            new_name='top_languages',
        ),
        migrations.RenameField(
            model_name='widgetslist2',
            old_name='volume_widget',
            new_name='volume',
        ),
    ]