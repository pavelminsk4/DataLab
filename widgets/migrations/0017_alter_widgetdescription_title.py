# Generated by Django 4.0.6 on 2022-12-09 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0016_widgetslist2_content_volume_top_10_source_widget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetdescription',
            name='title',
            field=models.CharField(default='Title', max_length=50),
        ),
    ]
