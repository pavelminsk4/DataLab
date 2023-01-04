# Generated by Django 4.0.6 on 2023-01-04 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0024_remove_widgetdescription_title_for_change_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widgetslist2',
            name='content_volume_top_10_authors_widget',
        ),
        migrations.RemoveField(
            model_name='widgetslist2',
            name='content_volume_top_10_countries_widget',
        ),
        migrations.RemoveField(
            model_name='widgetslist2',
            name='content_volume_top_10_source_widget',
        ),
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_5_authors_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_5_authors_widget', to='widgets.widgetdescription'),
        ),
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_5_countries_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_5_countries_widget', to='widgets.widgetdescription'),
        ),
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_5_source_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_5_source_widget', to='widgets.widgetdescription'),
        ),
    ]