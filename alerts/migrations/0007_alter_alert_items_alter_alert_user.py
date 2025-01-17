# Generated by Django 4.0.6 on 2023-04-28 13:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alerts', '0006_alertitem_remove_alert_module_project_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='alert', to='alerts.alertitem'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
