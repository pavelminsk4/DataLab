# Generated by Django 4.0.6 on 2022-11-16 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0006_dimensions_projectdimensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='widgetdescription',
            name='linked_dimensions',
            field=models.ManyToManyField(to='widgets.dimensions'),
        ),
        migrations.AlterField(
            model_name='dimensions',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]