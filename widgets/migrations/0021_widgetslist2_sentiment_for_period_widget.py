# Generated by Django 4.0.6 on 2022-12-15 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0020_widgetslist2_sentiment_top_10_authors_widget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetslist2',
            name='sentiment_for_period_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sentiment_for_period_widget', to='widgets.widgetdescription'),
        ),
    ]