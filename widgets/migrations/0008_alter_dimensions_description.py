# Generated by Django 4.0.6 on 2022-11-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('widgets', '0007_widgetdescription_linked_dimensions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dimensions',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
