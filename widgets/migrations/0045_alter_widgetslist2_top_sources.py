# Generated by Django 4.0.6 on 2023-06-26 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0044_rename_top_brands_widgetslist2_top_sources'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetslist2',
            name='top_sources',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='onl_top_sources', to='widgets.widgetdescription'),
        ),
    ]