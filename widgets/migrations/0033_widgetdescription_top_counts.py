# Generated by Django 4.0.6 on 2023-03-14 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0032_alter_widgetdescription_chart_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetdescription',
            name='top_counts',
            field=models.IntegerField(default=5),
        ),
    ]