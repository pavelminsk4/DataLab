# Generated by Django 4.0.6 on 2022-12-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0015_widgetslist2_top_10_languages_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_10_source_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_10_source_widget', to='widgets.widgetdescription'),
        ),
    ]
