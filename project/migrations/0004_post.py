# Generated by Django 4.0.6 on 2022-09-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_feedlinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.TextField(blank=True, null=True, verbose_name='entry_title')),
                ('entry_title_detail_type', models.TextField(blank=True, null=True, verbose_name='entry_title_detail_type')),
                ('entry_title_detail_language', models.TextField(blank=True, null=True, verbose_name='entry_title_detail_language')),
                ('entry_title_detail_base', models.TextField(blank=True, null=True, verbose_name='entry_title_detail_base')),
                ('entry_title_detail_value', models.TextField(blank=True, null=True, verbose_name='entry_title_detail_value')),
                ('entry_links_rel', models.TextField(blank=True, null=True, verbose_name='entry_links_rel')),
                ('entry_links_type', models.TextField(blank=True, null=True, verbose_name='entry_links_type')),
                ('entry_links_href', models.TextField(blank=True, null=True, verbose_name='entry_links_href')),
                ('entry_link', models.TextField(blank=True, null=True, verbose_name='Link')),
                ('entry_summary', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('creationdate', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('entry_summary_detail_type', models.TextField(blank=True, null=True, verbose_name='entry_Summary_detail_type')),
                ('entry_summary_detail_language', models.TextField(blank=True, null=True, verbose_name='entry_Summary_detail_language')),
                ('entry_summary_detail_base', models.TextField(blank=True, null=True, verbose_name='entry_title_Summary_base')),
                ('entry_summary_detail_value', models.TextField(blank=True, null=True, verbose_name='entry_title_Summary_value')),
                ('entry_published', models.TextField(blank=True, null=True, verbose_name='Published')),
                ('entry_published_parsed', models.TextField(blank=True, null=True, verbose_name='Published Parsed')),
                ('entry_id', models.TextField(blank=True, null=True, verbose_name='Entry ID')),
                ('entry_guidislink', models.TextField(blank=True, null=True, verbose_name='Guidislink')),
                ('entry_content_type', models.TextField(blank=True, null=True, verbose_name='entry_content_type')),
                ('entry_content_language', models.TextField(blank=True, null=True, verbose_name='entry_content_language')),
                ('entry_content_base', models.TextField(blank=True, null=True, verbose_name='entry_content_base')),
                ('entry_content_value', models.TextField(blank=True, null=True, verbose_name='entry_content_value')),
                ('entry_media_thumbnail_url', models.TextField(blank=True, null=True, verbose_name='entry_media_thumbnail_url')),
                ('entry_media_thumbnail_width', models.TextField(blank=True, null=True, verbose_name='entry_media_thumbnail_width')),
                ('entry_media_thumbnail_height', models.TextField(blank=True, null=True, verbose_name='entry_media_thumbnail_height')),
                ('entry_href', models.TextField(blank=True, null=True, verbose_name='entry_href')),
                ('entry_media_content_type', models.TextField(blank=True, null=True, verbose_name='entry_media_content_type')),
                ('entry_media_content_url', models.TextField(blank=True, null=True, verbose_name='entry_media_content_url')),
                ('entry_media_content_height', models.TextField(blank=True, null=True, verbose_name='entry_media_content_height')),
                ('entry_media_content_medium', models.TextField(blank=True, null=True, verbose_name='entry_media_content_medium')),
                ('entry_media_content_width', models.TextField(blank=True, null=True, verbose_name='entry_media_content_width')),
                ('entry_media_credit_content', models.TextField(blank=True, null=True, verbose_name='entry_media_credit_content')),
                ('entry_credit', models.TextField(blank=True, null=True, verbose_name='entry_credit')),
                ('entry_authors', models.TextField(blank=True, null=True, verbose_name='authors')),
                ('entry_author', models.TextField(blank=True, null=True, verbose_name='author')),
                ('entry_author_detail', models.TextField(blank=True, null=True, verbose_name='author_detail')),
                ('entry_tags_term', models.TextField(blank=True, null=True, verbose_name='entry_tags_term')),
                ('entry_tags_scheme', models.TextField(blank=True, null=True, verbose_name='entry_tags_scheme')),
                ('entry_tags_label', models.TextField(blank=True, null=True, verbose_name='entry_tags_label')),
                ('feed_title', models.TextField(blank=True, null=True, verbose_name='feed_title')),
                ('feed_title_detail_type', models.TextField(blank=True, null=True, verbose_name='feed_title_detail_type')),
                ('feed_title_detail_language', models.TextField(blank=True, null=True, verbose_name='feed_title_detail_language')),
                ('feed_title_detail_base', models.TextField(blank=True, null=True, verbose_name='feed_title_detail_base')),
                ('feed_title_detail_value', models.TextField(blank=True, null=True, verbose_name='feed_title_detail_value')),
                ('feed_links_rel', models.TextField(blank=True, null=True, verbose_name='feed_links_rel')),
                ('feed_links_type', models.TextField(blank=True, null=True, verbose_name='feed_links_type')),
                ('feed_links_href', models.TextField(blank=True, null=True, verbose_name='feed_links_href')),
                ('feed_link', models.TextField(blank=True, null=True, verbose_name='feed_link')),
                ('feed_image_title', models.TextField(blank=True, null=True, verbose_name='feed_image_title')),
                ('feed_image_title_detail_type', models.TextField(blank=True, null=True, verbose_name='feed_image_title_detail_type')),
                ('feed_image_title_detail_language', models.TextField(blank=True, null=True, verbose_name='feed_image_title_detail_language')),
                ('feed_image_title_detail_base', models.TextField(blank=True, null=True, verbose_name='feed_image_title_detail_base')),
                ('feed_image_title_detail_value', models.TextField(blank=True, null=True, verbose_name='feed_image_title_detail_value')),
                ('feed_image_href', models.TextField(blank=True, null=True, verbose_name='feed_image_href')),
                ('feed_image_link', models.TextField(blank=True, null=True, verbose_name='feed_image_link')),
                ('feed_image_links', models.TextField(blank=True, null=True, verbose_name='feed_image_links')),
                ('feed_subtitle', models.TextField(blank=True, null=True, verbose_name='feed_subtitle')),
                ('feed_subtitle_detail', models.TextField(blank=True, null=True, verbose_name='feed_subtitle_detail')),
                ('feed_language', models.TextField(blank=True, null=True, verbose_name='feed_language')),
                ('feed_rights', models.TextField(blank=True, null=True, verbose_name='feed_rights')),
                ('feed_rights_detail', models.TextField(blank=True, null=True, verbose_name='feed_rights_detail')),
                ('feed_updated', models.TextField(blank=True, null=True, verbose_name='feed_updated')),
                ('feed_updated_parsed', models.TextField(blank=True, null=True, verbose_name='feed_updated_parsed')),
                ('feed_published', models.TextField(blank=True, null=True, verbose_name='feed_published')),
                ('feed_published_parsed', models.TextField(blank=True, null=True, verbose_name='feed_published_parsed')),
                ('feed_tags_term', models.TextField(blank=True, null=True, verbose_name='feed_tags_term')),
                ('feed_tags_scheme', models.TextField(blank=True, null=True, verbose_name='feed_tags_scheme')),
                ('feed_tags_label', models.TextField(blank=True, null=True, verbose_name='feed_tags_label')),
                ('feed_tags_list', models.TextField(blank=True, null=True, verbose_name='feed_tags_list')),
                ('feed_ttl', models.TextField(blank=True, null=True, verbose_name='feed_ttl')),
                ('feed_docs', models.TextField(blank=True, null=True, verbose_name='feed_docs')),
                ('feed_generator_detail', models.TextField(blank=True, null=True, verbose_name='generator_detail')),
                ('feed_generator', models.TextField(blank=True, null=True, verbose_name='feed_generator')),
                ('feed_publisher', models.TextField(blank=True, null=True, verbose_name='feed_Publisher')),
                ('feed_publisher_detail', models.TextField(blank=True, null=True, verbose_name='feed_publisher_detail')),
                ('headers_date', models.TextField(blank=True, null=True, verbose_name='headers date')),
                ('publishdate', models.DateField(blank=True, null=True, verbose_name='Publish Date')),
                ('sentiment', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('usersentiment', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('updatedsentiment', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('is_sentiment', models.BooleanField(default=False)),
            ],
        ),
    ]