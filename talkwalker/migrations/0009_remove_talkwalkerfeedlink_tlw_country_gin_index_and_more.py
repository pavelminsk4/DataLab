# Generated by Django 4.0.6 on 2023-10-17 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talkwalker', '0008_alter_talkwalkerpost_category_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='talkwalkerfeedlink',
            name='tlw_country_gin_index',
        ),
        migrations.RemoveIndex(
            model_name='talkwalkerfeedlink',
            name='tlw_source1_gin_index',
        ),
    ]
