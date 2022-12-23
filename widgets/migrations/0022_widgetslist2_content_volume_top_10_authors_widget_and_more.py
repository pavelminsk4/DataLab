# Generated by Django 4.0.6 on 2022-12-19 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0021_widgetslist2_sentiment_for_period_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_10_authors_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_10_authors_widget', to='widgets.widgetdescription'),
        ),
        migrations.AddField(
            model_name='widgetslist2',
            name='content_volume_top_10_countries_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_volume_top_10_countries_widget', to='widgets.widgetdescription'),
        ),
    ]