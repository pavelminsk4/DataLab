from talkwalker.services.retrieve_status_of_the_task import retrieve_status_of_the_task
from talkwalker.services.create_target_collector import create_target_collector
from talkwalker.services.delete_a_collector import delete_collector
from talkwalker.services.read_a_collector import read_collector
from talkwalker.services.new_task_on_a_query import new_task
from talkwalker.services.get_tw_query import get_tw_query
from talkwalker.services.create_post import create_post
from talkwalker.classes.livestream import Livestream
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from project.models import Project
from project.models import Speech
from django.db import models
import json


class TalkwalkerFeedlink(models.Model):
    country = models.CharField('Country',max_length=200,null=True,blank=True)
    source1 = models.CharField('Source1',max_length=200,null=True,blank=True)
    sourceurl = models.URLField(max_length=200,null=True,blank=True)
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


def check_status(task_id):
     i = 0
     while i < 200:
        i = i + 1
        status = retrieve_status_of_the_task(task_id)
        if status == 'result_limit_reached':
            break


def fetch_posts(start_date, end_date, limit, keywords, target):
    create_target_collector()
    task_id = new_task(start_date, end_date, limit, keywords, target)
    check_status(task_id)
    lines = read_collector()
    for line in lines:
        create_post(line)
    delete_collector()


from django_celery_beat.models import PeriodicTask, CrontabSchedule

@receiver(post_save, sender=Project)
def create_periodic_task(sender, instance, created, **kwargs):
  if created:
      Livestream(instance.id).create()
      crontab_schedule = CrontabSchedule.objects.create(
        minute = '*/5',
        hour = '*',
        day_of_week = '*',
        day_of_month = '*',
      )
      instance.hourly_crontab_schedule = crontab_schedule
      periodic_task = PeriodicTask.objects.create(
        crontab = crontab_schedule,
        name = f'LiveSearch_project_{instance.id}',
        task = 'talkwalker.tasks.livesearch_sender',
        args = json.dumps([instance.id]),
      )
      instance.hourly_periodic_task = periodic_task


@receiver(post_save, sender=Project)
def fetch_talkwalker_posts(sender, instance, created, **kwargs):
    fetch_posts(
        instance.start_search_date,
        instance.end_search_date,
        5000,
        get_tw_query(instance),
        'datalab'
    )

@receiver(pre_delete, sender=Project)
def delete_livestream(sender, instance, **kwargs):
    Livestream(instance.id).delete()
