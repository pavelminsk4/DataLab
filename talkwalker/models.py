from talkwalker.services.retrieve_status_of_the_task import retrieve_status_of_the_task
from talkwalker.services.create_target_collector import create_target_collector
from talkwalker.services.delete_a_collector import delete_collector
from talkwalker.services.new_task_on_a_query import new_task
from talkwalker.services.read_a_collector import read_collector
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.models import Project
from project.models import Speech
from langcodes import Language
from django.db import models
from pprint import pprint
import json
from datetime import datetime


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


def add_language(language_code):
    title = Language.get(language_code).display_name()
    return Speech.objects.get_or_create(language=title)[0]


def define_sentiment(value):
    sent = 'neutral'
    if value<0:
        sent = 'negative'
    if value>0:
        sent = 'positive'
    return sent



def create_post(line):
    print('-------->create_post')
    try:
        data = json.loads(line)['chunk_result']['data']['data']
    except:
        pass
    try:
        acountry=data['extra_source_attributes']['world_data']['country']
    except:
        acountry=''
    try:
        asourceurl=data['host_url']
    except:
        asourceurl=''
    try:
        aalexaglobalrank=data['reach']
    except:
        aalexaglobalrank=0
    try:
        asource1=data['extra_source_attributes']['name']
    except:
        asource1=''
    try:
        aentry_title=data['title']
    except:
        aentry_title=''
    try:
        aentry_summary=data['content']
    except:
        aentry_summary=''
    try:
        afeed_language=add_language(data['lang'])
    except:
        afeed_language=''
    try:
        aentry_media_content_url=data['images'][0]['url']
    except:
        aentry_media_content_url=''
    try:
        aentry_links_href=data['url']
    except:
        aentry_links_href=''
    try:
        aentry_author=data['extra_source_attributes']['name']
    except:
        aentry_author=''
    try:
        aentry_published=datetime.fromtimestamp(data['published']/1000)
    except:
        aentry_published=datetime.now()
    try:
        asentiment=define_sentiment(data['sentiment'])
    except:
        asentiment='neutral'
    try:
        acategory=data['tokens_content'][0]
    except:
        acategory=''
    try:
        fl = TalkwalkerFeedlink.objects.create(
            country=acountry,
            sourceurl=asourceurl,
            alexaglobalrank=aalexaglobalrank,
            source1=asource1,
        )
        post = TalkwalkerPost.objects.create(
            entry_title=aentry_title,
            entry_summary=aentry_summary,
            feed_language=afeed_language,
            entry_media_content_url=aentry_media_content_url,            
            entry_links_href=aentry_links_href,
            entry_author=aentry_author,
            entry_published=aentry_published,
            sentiment=asentiment,
            category=acategory,
            feedlink=fl,
        )
    except:
       print('------->except')
       pass


def check_status(task_id):
     i =0
     while i<200:
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


@receiver(post_save, sender=Project)
def fetch_talkwalker_posts(sender, instance, created, **kwargs):
    fetch_posts(
        instance.start_search_date,
        instance.end_search_date,
        1000,
        instance.keywords,
        'datalab'
    )
