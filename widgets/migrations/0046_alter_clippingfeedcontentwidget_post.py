# Generated by Django 4.0.6 on 2023-10-02 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talkwalker', '0007_talkwalkerfeedlink_tlw_country_gin_index_and_more'),
        ('widgets', '0045_alter_widgetslist2_top_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clippingfeedcontentwidget',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='talkwalker.talkwalkerpost', verbose_name='Post'),
        ),
    ]