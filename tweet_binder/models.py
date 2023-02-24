from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from .services.historical_search import *
from .services.live_search import *
from .services.get_report_state import *
from .services.get_publications import *
from .services.delete_report import *
from .services.basic_search import *
from .services.login import *
from django.db import models

import time
import os
import json

class TweetBinderPost(models.Model):
  post_id = models.CharField(max_length=20, unique=True)
  async_ops = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  binders = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  count_textlength = models.IntegerField(blank=True, null=True)
  count_sentiment = models.IntegerField(blank=True, null=True)
  count_retweets = models.IntegerField(blank=True, null=True)
  count_totalretweets = models.IntegerField(blank=True, null=True)
  count_favorites = models.IntegerField(blank=True, null=True)
  count_hashtags = models.IntegerField(blank=True, null=True)
  count_images = models.IntegerField(blank=True, null=True)
  count_links = models.IntegerField(blank=True, null=True)
  count_linksandimages = models.IntegerField(blank=True, null=True)
  count_mentions = models.IntegerField(blank=True, null=True)
  count_originals = models.IntegerField(blank=True, null=True)
  count_clears = models.IntegerField(blank=True, null=True)
  count_replies = models.IntegerField(blank=True, null=True)
  count_publicationscore = models.IntegerField(blank=True, null=True)
  count_uservalue = models.FloatField(blank=True, null=True)
  count_tweetvalue = models.FloatField(blank=True, null=True)
  createdat = models.IntegerField(blank=True, null=True)
  favorites = models.IntegerField(blank=True, null=True)
  hashtags = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  images = ArrayField(models.CharField(max_length=200), blank=True, null=True)
  inreplyto = models.CharField(max_length=100, blank=True, null=True)
  inreplytoid = models.CharField(max_length=100, blank=True, null=True)
  language = models.CharField(max_length=50, blank=True, null=True)
  links = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  mentions = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  locationString = models.CharField(max_length=50, blank=True, null=True)
  retweets = models.IntegerField(blank=True, null=True)
  sentiment_vote = models.CharField(max_length=50, blank=True, null=True)
  source = models.CharField(max_length=50, blank=True, null=True)
  text = models.CharField(max_length=10000, blank=True, null=True)
  type = ArrayField(models.CharField(max_length=100), blank=True, null=True)
  updatedat = models.IntegerField(blank=True, null=True)
  user_id = models.CharField(max_length=50, blank=True, null=True)
  user_name = models.CharField(max_length=100, blank=True, null=True)
  user_alias = models.CharField(max_length=100, blank=True, null=True)
  user_picture = models.CharField(max_length=300, blank=True, null=True)
  user_followers = models.IntegerField(blank=True, null=True)
  user_following = models.IntegerField(blank=True, null=True)
  user_verified = models.BooleanField(default=False)
  user_bio = models.CharField(max_length=1000, blank=True, null=True)
  user_age = models.IntegerField(blank=True, null=True)
  user_counts_lists = models.IntegerField(blank=True, null=True)
  user_statuses = models.IntegerField(blank=True, null=True)
  user_location = models.CharField(max_length=100, blank=True, null=True)
  user_gender = models.CharField(max_length=20, blank=True, null=True)
  user_value = models.FloatField(blank=True, null=True)
  videos = ArrayField(models.CharField(max_length=200), blank=True, null=True)

class TypesOfSearch(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  limit = models.IntegerField(blank=True, null=True, default=10)
  keyword = models.CharField(max_length=100, blank=False, null=False)

  
  class Meta:
    abstract = True

class HistoricalSearchProject(TypesOfSearch):
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  
  def __str__(self):
      return self.title

@receiver(post_save, sender=HistoricalSearchProject)
def create_historical_search_project(sender, instance, created, **kwargs):
  if created:
    keyword = instance.keyword
    limit = instance.limit
    start_date = instance.start_date
    end_date = instance.end_date
    instance.save()
    historical_search_type(keyword, limit, start_date, end_date)

class BasicSearchProject(TypesOfSearch):

  def __str__(self):
      return self.title

@receiver(post_save, sender=BasicSearchProject)
def create_historical_search_project(sender, instance, created, **kwargs):
  if created:
    keyword = instance.keyword
    limit = instance.limit
    instance.save()
    basic_search_type(keyword, limit)          

class LiveSearchProject(TypesOfSearch):

  def __str__(self):
      return self.title

@receiver(post_save, sender=LiveSearchProject)
def create_live_search_project(sender, instance, created, **kwargs):
  if created:
    keyword = instance.keyword
    limit = instance.limit
    instance.save()
    live_search_type(keyword, limit)    

email = os.environ.get("EMAIL_TWEET")
password = os.environ.get("PASSWORD_TWEET")
api_route = os.environ.get("API_ROUTE")

def basic_search_type(keyword, limit):
    basic_search_url = api_route + '/search/twitter/7-day'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(basic_search(keyword, limit, auth_token, basic_search_url))["resourceId"]
    time.sleep(5)
    search(report_id, auth_token)

def historical_search_type(keyword, limit, start_date, end_date):
    historical_search_url = api_route + '/search/twitter/historical'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(historical_search(keyword, limit, start_date, end_date, auth_token, historical_search_url))["resourceId"]
    time.sleep(60)
    search(report_id, auth_token)   

def live_search_type(keyword, limit):
    live_search_url = api_route + '/search/twitter/live'
    auth_token = json.loads(login(email, password))['authToken'] 
    live_search(keyword, limit, auth_token, live_search_url)
 
def search(report_id, auth_token):
    data_report_state = json.loads(get_report_state(report_id, auth_token))
    print(data_report_state)
    if json.loads(get_report_state(report_id, auth_token))['status'] == "generated":
        data_tweets = json.loads(get_publications(report_id, auth_token))['data']
        tweets = []
        for tweet in data_tweets:
            new_tweet = {
                'post_id': tweet['_id'],
                'async_ops': tweet['asyncOps'],
                'binders': tweet['binders'],
                'count_textlength': int(tweet['counts']['textLength']),
                'count_sentiment': tweet['counts']['sentiment'],
                'count_retweets': tweet['counts']['retweets'],
                'count_totalretweets': tweet['counts']['totalRetweets'],
                'count_favorites': tweet['counts']['favorites'],
                'count_hashtags': tweet['counts']['hashtags'],
                'count_images': tweet['counts']['images'],
                'count_links': tweet['counts']['links'],
                'count_linksandimages': tweet['counts']['linksAndImages'], 
                'count_mentions': tweet['counts']['mentions'], 
                'count_originals': tweet['counts']['originals'], 
                'count_clears': tweet['counts']['clears'],
                'count_replies': tweet['counts']['replies'],
                'count_publicationscore': tweet['counts']['publicationScore'], 
                'count_uservalue': tweet['counts']['userValue'], 
                'count_tweetvalue': tweet['counts']['tweetValue'], 
                'createdat': tweet['createdAt'], 
                'favorites': tweet['favorites'], 
                'hashtags': tweet['hashtags'], 
                'images': tweet['images'], 
                'inreplyto': tweet['inReplyTo'],  
                'inreplytoid': tweet['inReplyToId'],  
                'language': tweet['lang'],  
                'links': tweet['links'],  
                'mentions': tweet['mentions'],  
                'locationString': tweet['rawLocation']['locationString'],  
                'retweets': tweet['retweets'],  
                'sentiment_vote': tweet['sentiment']['vote'],  
                'source': tweet['source'],  
                'text': tweet['text'],  
                'type': tweet['type'],  
                'updatedat': tweet['updatedAt'],  
                'user_id': tweet['user']['id'],  
                'user_name': tweet['user']['name'],  
                'user_alias': tweet['user']['alias'], 
                'user_picture': tweet['user']['picture'],
                'user_followers': tweet['user']['followers'], 
                'user_following': tweet['user']['following'], 
                'user_verified': tweet['user']['verified'], 
                'user_bio': tweet['user']['bio'], 
                'user_age': tweet['user']['age'], 
                'user_counts_lists':tweet['user']['counts']['lists'], 
                'user_statuses': tweet['user']['counts']['statuses'], 
                'user_location': tweet['user']['location'],
                'user_gender': tweet['user']['gender'], 
                'user_value': tweet['user']['value'],
                'videos': tweet['videos'],
            }
            tweets.append(new_tweet)
        try:
            django_list = [TweetBinderPost(**vals) for vals in tweets if not TweetBinderPost.objects.filter(post_id=vals['post_id'])] 
            TweetBinderPost.objects.bulk_create(django_list)
        except:
            print('error!!!')
            pass
        tweets = []
    else:
       print('Report not generated') 
       print(json.loads(get_report_state(report_id, auth_token))['status'])

    delete_report(auth_token, report_id)
