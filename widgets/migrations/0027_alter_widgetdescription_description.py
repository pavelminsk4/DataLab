# Generated by Django 4.0.6 on 2023-01-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0026_clippingfeedcontentwidget_clipping widget uniqueness constraint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetdescription',
            name='description',
            field=models.TextField(default=''),
        ),
    ]