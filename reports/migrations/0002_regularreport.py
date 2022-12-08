# Generated by Django 4.0.6 on 2022-12-08 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_celery_beat', '0016_alter_crontabschedule_timezone'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegularReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('email_title', models.TextField(max_length=500)),
                ('ending_date', models.DateTimeField()),
                ('type', models.CharField(max_length=10)),
                ('crontab_schedule', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.crontabschedule')),
                ('periodic_task', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_celery_beat.periodictask')),
                ('template', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reports.templates')),
                ('user', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
