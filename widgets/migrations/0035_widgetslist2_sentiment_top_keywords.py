# Generated by Django 4.0.6 on 2023-03-20 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0034_widgetslist2_top_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetslist2',
            name='sentiment_top_keywords',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sentiment_top_keywords', to='widgets.widgetdescription'),
        ),
    ]
