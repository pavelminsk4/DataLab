# Generated by Django 4.0.6 on 2022-12-06 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0012_remove_widgetslist2_clipping_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetslist2',
            name='top_10_brands_widget',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='top_10_brands_widg_description', to='widgets.widgetdescription'),
        ),
    ]