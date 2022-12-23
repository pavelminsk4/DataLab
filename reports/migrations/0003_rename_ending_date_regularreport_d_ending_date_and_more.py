# Generated by Django 4.0.6 on 2022-12-21 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0016_alter_crontabschedule_timezone'),
        ('reports', '0002_regularreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regularreport',
            old_name='ending_date',
            new_name='d_ending_date',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='crontab_schedule',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='day_of_month',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='day_of_week',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='minute',
        ),
        migrations.RemoveField(
            model_name='regularreport',
            name='periodic_task',
        ),
        migrations.AddField(
            model_name='regularreport',
            name='d_day_of_month',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='d_day_of_week',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='d_hour',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='d_minute',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='daily_crontab_schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_d_crontab_sch', to='django_celery_beat.crontabschedule'),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='daily_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='daily_periodic_task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_d_periodic_task', to='django_celery_beat.periodictask'),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='h_day_of_month',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='h_day_of_week',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='h_ending_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='h_hour',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='h_minute',
            field=models.CharField(default='*', max_length=4),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='hourly_crontab_schedule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_h_crontab_sch', to='django_celery_beat.crontabschedule'),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='hourly_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='regularreport',
            name='hourly_periodic_task',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_h_periodic_task', to='django_celery_beat.periodictask'),
        ),
    ]