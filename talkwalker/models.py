from talkwalker.classes.livestream import Livestream
from talkwalker.classes.asker import Asker

from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from project.models import Project
from project.models import Speech
from django.db import models
import json


class TalkwalkerFeedlink(models.Model):
    country = models.CharField('Country', max_length=200, null=True, blank=True)
    source1 = models.CharField('Source1', max_length=200, null=True, blank=True)
    sourceurl = models.URLField(max_length=200, null=True, blank=True)
    alexaglobalrank = models.BigIntegerField(default=0)


class TalkwalkerPost(models.Model):
    entry_title = models.TextField('entry_title')
    entry_published = models.DateTimeField(null=True,blank=True)
    entry_summary = models.TextField('Summary',null=True,blank=True)
    entry_media_thumbnail_url = models.TextField('entry_media_thumbnail_url',null=True,blank=True)
    entry_media_content_url = models.TextField('entry_media_content_url',null=True,blank=True)
    feed_image_href = models.TextField('feed_image_href',null=True,blank=True)
    feed_image_link = models.TextField('feed_image_link',null=True,blank=True)
    feed_language = models.ForeignKey(Speech,related_name='tw_speech',on_delete=models.CASCADE,null=True,blank=True)
    entry_author = models.TextField('authors',null=True,blank=True)
    entry_links_href = models.TextField('entry_links_href',null=True,blank=True)
    feedlink = models.ForeignKey(TalkwalkerFeedlink,on_delete=models.CASCADE,related_name='feedlink_feedsin',null=True,blank=True)
    sentiment = models.CharField('sentiment', max_length=8, default='neutral',null=True,blank=True)
    category = models.TextField('Category',null=True,blank=True)

    def __str__(self):
        return self.entry_title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['entry_title', 'feedlink_id'], name='talkwalker post uniqueness constraint')
        ]


@receiver(post_save, sender=Project)
def create_periodic_task(sender, instance, created, **kwargs):
    if created:
        Livestream(instance.id).create()
        crontab_schedule = CrontabSchedule.objects.create(
            minute='*/5',
            hour='*',
            day_of_week='*',
            day_of_month='*',
        )
        PeriodicTask.objects.create(
            crontab=crontab_schedule,
            name=f'LiveSearch_project_{instance.id}',
            task='talkwalker.tasks.livesearch_sender',
            args=json.dumps([instance.id]),
        )


@receiver(post_save, sender=Project)
def fetch_talkwalker_posts(sender, instance, created, **kwargs):
    Asker(instance.id, 'onl').run()


@receiver(pre_delete, sender=Project)
def delete_livestream(sender, instance, **kwargs):
    Livestream(instance.id).delete()
