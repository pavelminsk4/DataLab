# Generated by Django 4.0.6 on 2023-10-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talkwalker', '0007_talkwalkerfeedlink_tlw_country_gin_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkwalkerpost',
            name='category',
            field=models.TextField(blank=True, null=True, verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='talkwalkerpost',
            name='entry_summary',
            field=models.TextField(blank=True, null=True, verbose_name='summary'),
        ),
    ]