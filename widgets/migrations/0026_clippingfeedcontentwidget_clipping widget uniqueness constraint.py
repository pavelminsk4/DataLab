# Generated by Django 4.0.6 on 2023-01-09 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0025_remove_widgetslist2_content_volume_top_10_authors_widget_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='clippingfeedcontentwidget',
            constraint=models.UniqueConstraint(fields=('project_id', 'post_id'), name='clipping widget uniqueness constraint'),
        ),
    ]
