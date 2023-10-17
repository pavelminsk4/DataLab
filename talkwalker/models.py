from talkwalker.classes.livestream import Livestream
from talkwalker.classes.asker import Asker

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save, pre_delete, post_init
from django.dispatch import receiver
from project.models import Project
from project.models import Speech
from django.db import models
import json

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db.models.functions import Upper

import environ

env = environ.Env()
ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]


class TalkwalkerFeedlink(models.Model):
    country = models.CharField('Country', max_length=200, null=True, blank=True)
    source1 = models.CharField('Source1', max_length=200, null=True, blank=True)
    sourceurl = models.URLField(max_length=200, null=True, blank=True)
    alexaglobalrank = models.BigIntegerField(default=0)


class TalkwalkerPost(models.Model):
    entry_title               = models.TextField('entry_title')
    entry_published           = models.DateTimeField(null=True, blank=True)
    entry_summary             = models.TextField('summary', null=True, blank=True)
    entry_media_thumbnail_url = models.TextField('entry_media_thumbnail_url', null=True, blank=True)
    entry_media_content_url   = models.TextField('entry_media_content_url', null=True, blank=True)
    feed_image_href           = models.TextField('feed_image_href', null=True, blank=True)
    feed_image_link           = models.TextField('feed_image_link', null=True, blank=True)
    feed_language             = models.ForeignKey(Speech, related_name='tw_speech', on_delete=models.CASCADE, null=True, blank=True)
    entry_author              = models.TextField('authors', null=True, blank=True)
    entry_links_href          = models.TextField('entry_links_href', null=True, blank=True)
    feedlink                  = models.ForeignKey(TalkwalkerFeedlink, on_delete=models.CASCADE, related_name='feedlink_feedsin', null=True, blank=True)
    sentiment                 = models.CharField('sentiment', max_length=8, default='neutral', null=True, blank=True)
    category                  = models.TextField('category', null=True, blank=True)
    full_text                 = models.TextField('full_text', null=True, blank=True)

    def __str__(self):
        return self.entry_title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entry_title', 'feedlink_id'], name='talkwalker post uniqueness constraint')
        ]
        indexes = [
            models.Index(fields=['entry_published']),
            models.Index(fields=['feedlink']),
            models.Index(fields=['entry_author']),
            models.Index(fields=['feed_language']),
            models.Index(fields=['sentiment']),
            GinIndex(
                OpClass(Upper('entry_title'), name='gin_trgm_ops'),
                name='tlw_entry_title_gin_index',
            ),
            GinIndex(
                OpClass(Upper('entry_summary'), name='gin_trgm_ops'),
                name='tlw_entry_summary_gin_index',
            ),
            GinIndex(
                OpClass(Upper('entry_author'), name='gin_trgm_ops'),
                name='tlw_entry_author_gin_index',
            )
        ]


@receiver(post_save, sender='twenty_four_seven.ProjectTwentyFourSeven')
@receiver(post_save, sender=Project)
def create_periodic_task(sender, instance, created, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost' and created:
        Livestream(instance.id, sender.__name__).create()
        crontab_schedule = CrontabSchedule.objects.create(
            minute='*/20',
            hour='*',
            day_of_week='*',
            day_of_month='*',
        )
        PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name=f'LiveSearch_project_{instance.id}',
            task='talkwalker.tasks.livesearch_sender',
            args=json.dumps([instance.id, sender.__name__]),
        )


@receiver(post_save, sender='twenty_four_seven.ProjectTwentyFourSeven')
def tfs_items(sender, instance, created, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost' and created:
        crontab_schedule = CrontabSchedule.objects.create(
            minute='*/10',
            hour='*',
            day_of_week='*',
            day_of_month='*',
        )
        PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name=f'Attach_items_tfs_{instance.id}',
            task='twenty_four_seven.models.attach_online_posts',
            args=json.dumps([instance.id]),
        )


@receiver(post_save, sender='twenty_four_seven.ProjectTwentyFourSeven')
@receiver(post_save, sender=Project)
def fetch_talkwalker_posts(sender, instance, created, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost' and created:
        Asker(instance.id, sender.__name__).run()


@receiver(pre_delete, sender=Project)
@receiver(pre_delete, sender='twenty_four_seven.ProjectTwentyFourSeven')
def delete_livestream(sender, instance, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost':
        Livestream(instance.id, sender.__name__).delete()


@receiver(pre_delete, sender='twenty_four_seven.ProjectTwentyFourSeven')
def delete_periodic_tasks(sender, instance, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost':
        tasks = PeriodicTask.objects.filter(name=f'Attach_items_tfs_{instance.id}')
        tasks.delete()


@receiver(pre_delete, sender=Project)
@receiver(pre_delete, sender='twenty_four_seven.ProjectTwentyFourSeven')
def delete_live_search_periodic_tasks(sender, instance, **kwargs):
    if ALLOWED_HOSTS[0] != 'localhost':
        tasks = PeriodicTask.objects.filter(name=f'LiveSearch_project_{instance.id}')
        tasks.delete()
