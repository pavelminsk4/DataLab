# Generated by Django 4.0.6 on 2022-11-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0008_widgetdescription_author_dim_pivot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetdescription',
            name='linked_dimensions',
            field=models.ManyToManyField(blank=True, to='widgets.dimensions'),
        ),
    ]