from django.db import models
from django.contrib.auth.models import User
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import json


class Templates(models.Model):
    title = models.CharField(max_length=50)
    layout_file = models.FileField(upload_to='static/report_templates')

    def __str__(self):
        return self.title


class ReportItem(models.Model):
    MODULE_TYPE_CHOICES = [
        ('Project', 'Online'),
        ('ProjectSocial', 'Social'),
    ]

    module_type       = models.CharField(max_length=70)
    module_project_id = models.IntegerField(blank=True, null=True)

    onl_summary                      = models.BooleanField(default=False)
    onl_volume                       = models.BooleanField(default=False)
    onl_clipping_feed_content        = models.BooleanField(default=False)
    onl_top_authors                  = models.BooleanField(default=False)
    onl_top_sources                  = models.BooleanField(default=False)
    onl_top_countries                = models.BooleanField(default=False)
    onl_top_languages                = models.BooleanField(default=False)
    onl_content_volume_top_sources   = models.BooleanField(default=False)
    onl_sentiment_top_sources        = models.BooleanField(default=False)
    onl_sentiment_top_countries      = models.BooleanField(default=False)
    onl_sentiment_top_authors        = models.BooleanField(default=False)
    onl_sentiment_top_languages      = models.BooleanField(default=False)
    onl_sentiment_for_period         = models.BooleanField(default=False)
    onl_content_volume_top_authors   = models.BooleanField(default=False)
    onl_content_volume_top_countries = models.BooleanField(default=False)
    onl_top_keywords                 = models.BooleanField(default=False)
    onl_sentiment_top_keywords       = models.BooleanField(default=False)
    onl_sentiment_number_of_results  = models.BooleanField(default=False)
    onl_sentiment_diagram            = models.BooleanField(default=False)
    onl_authors_by_country           = models.BooleanField(default=False)
    onl_top_sharing_sources          = models.BooleanField(default=False)
    onl_overall_top_sources          = models.BooleanField(default=False)
    onl_sources_by_country           = models.BooleanField(default=False)
    onl_sources_by_language          = models.BooleanField(default=False)
    onl_authors_by_language          = models.BooleanField(default=False)
    onl_authors_by_sentiment         = models.BooleanField(default=False)
    onl_overall_top_authors          = models.BooleanField(default=False)
    onl_languages_by_country         = models.BooleanField(default=False)
    onl_keywords_by_country          = models.BooleanField(default=False)

    soc_summary                      = models.BooleanField(default=False)
    soc_clipping_feed_content        = models.BooleanField(default=False)
    soc_top_locations                = models.BooleanField(default=False)
    soc_top_authors                  = models.BooleanField(default=False)
    soc_top_languages                = models.BooleanField(default=False)
    soc_content_volume               = models.BooleanField(default=False)
    soc_content_volume_top_locations = models.BooleanField(default=False)
    soc_content_volume_top_authors   = models.BooleanField(default=False)
    soc_content_volume_top_languages = models.BooleanField(default=False)
    soc_sentiment                    = models.BooleanField(default=False)
    soc_gender_volume                = models.BooleanField(default=False)
    soc_sentiment_number_of_results  = models.BooleanField(default=False)
    soc_sentiment_authors            = models.BooleanField(default=False)
    soc_sentiment_locations          = models.BooleanField(default=False)
    soc_sentiment_languages          = models.BooleanField(default=False)
    soc_sentiment_by_gender          = models.BooleanField(default=False)
    soc_top_keywords                 = models.BooleanField(default=False)
    soc_sentiment_top_keywords       = models.BooleanField(default=False)
    soc_sentiment_diagram            = models.BooleanField(default=False)
    soc_top_sharing_sources          = models.BooleanField(default=False)
    soc_overall_top_authors          = models.BooleanField(default=False)
    soc_top_authors_by_gender        = models.BooleanField(default=False)
    soc_authors_by_language          = models.BooleanField(default=False)
    soc_authors_by_location          = models.BooleanField(default=False)
    soc_authors_by_sentiment         = models.BooleanField(default=False)
    soc_authors_by_gender            = models.BooleanField(default=False)
    soc_gender_by_location           = models.BooleanField(default=False)
    soc_keywords_by_location         = models.BooleanField(default=False)
    soc_languages_by_location        = models.BooleanField(default=False)


class RegularReport(models.Model):
    title                    = models.CharField(max_length=50)
    department               = models.ForeignKey('accounts.department', on_delete=models.SET_NULL, null=True)
    project                  = models.ForeignKey('project.Project', on_delete=models.SET_NULL, null=True, blank=True)
    creator                  = models.ForeignKey(User, related_name='regular_report_creator', on_delete=models.SET_NULL, null=True)
    user                     = models.ManyToManyField(User, blank=True)
    email_title              = models.TextField(max_length=500, null=True, blank=True)
    h_template               = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_template')
    h_minute                 = models.CharField(max_length=4, default='*')
    h_hour                   = models.CharField(max_length=4, default='*')
    h_day_of_week            = models.CharField(max_length=4, default='*')
    h_day_of_month           = models.CharField(max_length=4, default='*')
    h_ending_date            = models.DateTimeField(null=True, blank=True)
    hourly_periodic_task     = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_periodic_task')
    hourly_crontab_schedule  = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_h_crontab_sch')
    hourly_enabled           = models.BooleanField(default=False)
    d_template               = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_template')
    d_minute                 = models.CharField(max_length=4, default='*')
    d_hour                   = models.CharField(max_length=4, default='*')
    d_day_of_week            = models.CharField(max_length=4, default='*')
    d_day_of_month           = models.CharField(max_length=4, default='*')
    d_ending_date            = models.DateTimeField(null=True, blank=True)
    daily_periodic_task      = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_periodic_task')
    daily_crontab_schedule   = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_d_crontab_sch')
    daily_enabled            = models.BooleanField(default=False)
    w_template               = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_template')
    w_minute                 = models.CharField(max_length=4, default='*')
    w_hour                   = models.CharField(max_length=4, default='*')
    w_day_of_week            = models.CharField(max_length=4, default='*')
    w_day_of_month           = models.CharField(max_length=4, default='*')
    w_ending_date            = models.DateTimeField(null=True, blank=True)
    weekly_periodic_task     = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_periodic_task')
    weekly_crontab_schedule  = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_w_crontab_sch')
    weekly_enabled           = models.BooleanField(default=False)
    m_template               = models.ForeignKey(Templates, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_template')
    m_minute                 = models.CharField(max_length=4, default='*')
    m_hour                   = models.CharField(max_length=4, default='*')
    m_day_of_week            = models.CharField(max_length=4, default='*')
    m_day_of_month           = models.CharField(max_length=4, default='*')
    m_ending_date            = models.DateTimeField(null=True, blank=True)
    monthly_periodic_task    = models.OneToOneField(PeriodicTask, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_periodic_task')
    monthly_crontab_schedule = models.OneToOneField(CrontabSchedule, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_m_crontab_sch')
    monthly_enabled          = models.BooleanField(default=False)
    report_template          = models.ForeignKey(Templates, related_name='regular_report_templates', on_delete=models.SET_NULL, null=True, blank=True)
    report_format            = models.CharField(max_length=3, default='pdf', blank=True)
    report_language          = models.CharField(max_length=10, default='English')
    created_at               = models.DateTimeField(auto_now_add=True)
    updated_at               = models.DateTimeField(auto_now=True)
    items                    = models.ManyToManyField(ReportItem, blank=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=RegularReport)
def create_periodic_task(sender, instance, created, **kwargs):
    if not created:
        return

    if instance.hourly_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
            minute='0',
            hour='*' if instance.h_hour == '*' else '*/' + str(instance.h_hour),
            day_of_week=instance.h_day_of_week,
            day_of_month=instance.h_day_of_month,
        )
        instance.hourly_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name='REGULAR_REPORT_' + instance.title + str(datetime.now()),
            task='reports.tasks.regular_report_sender',
            args=json.dumps([instance.id, 'hourly']),
        )
        instance.hourly_periodic_task = periodic_task

    if instance.daily_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
            minute=instance.d_minute,
            hour=instance.d_hour,
            day_of_week=instance.d_day_of_week,
            day_of_month=instance.d_day_of_month,
        )
        instance.daily_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name='REGULAR_REPORT_' + instance.title + str(datetime.now()),
            task='reports.tasks.regular_report_sender',
            args=json.dumps([instance.id, 'daily']),
        )
        instance.daily_periodic_task = periodic_task

    if instance.weekly_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
            minute=instance.w_minute,
            hour=instance.w_hour,
            day_of_week=instance.w_day_of_week,
            day_of_month=instance.w_day_of_month,
        )
        instance.weekly_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name='REGULAR_REPORT_' + instance.title + str(datetime.now()),
            task='reports.tasks.regular_report_sender',
            args=json.dumps([instance.id, 'weekly']),
        )
        instance.weekly_periodic_task = periodic_task

    if instance.monthly_enabled:
        crontab_schedule = CrontabSchedule.objects.create(
            minute=instance.m_minute,
            hour=instance.m_hour,
            day_of_week=instance.m_day_of_week,
            day_of_month=instance.m_day_of_month,
        )
        instance.monthly_crontab_schedule = crontab_schedule
        periodic_task = PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name='REGULAR_REPORT_' + instance.title + str(datetime.now()),
            task='reports.tasks.regular_report_sender',
            args=json.dumps([instance.id, 'monthly']),
        )
        instance.monthly_periodic_task = periodic_task

    instance.save()
