from account_analysis.models import ProjectAccountAnalysis
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from .services.get_user_tracker_stats import *
from .services.greate_user_tracker import *
from .services.stop_user_trackers import *
from .services.historical_search import *
from .services.get_report_state import *
from .services.get_publications import *
from .services.delete_report import *
from .services.basic_search import *
from .services.live_search import *
from celery import shared_task
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
  creation_date = models.DateTimeField()
  date = models.DateTimeField()
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
  sentiment = models.CharField(max_length=50, blank=True, null=True)
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
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.post_id

class TypesOfSearch(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  limit = models.IntegerField(blank=True, null=True, default=10)
  keyword = models.CharField(max_length=100, blank=False, null=False)
  keyword_and = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords AND')
  keyword_or = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords OR')
  keyword_nor = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords excluded')

  
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
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    start_date = instance.start_date
    end_date = instance.end_date
    historical_search_type(keyword, keyword_and, keyword_or, keyword_nor, limit, start_date, end_date)

class BasicSearchProject(TypesOfSearch):

  def __str__(self):
      return self.title

@receiver(post_save, sender=BasicSearchProject)
def create_basic_search_project(sender, instance, created, **kwargs):
  if created:
    keyword = instance.keyword
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    basic_search_type(keyword, keyword_and, keyword_or, keyword_nor, limit)          

class LiveSearchProject(TypesOfSearch):

  def __str__(self):
      return self.title

@receiver(post_save, sender=LiveSearchProject)
def create_live_search_project(sender, instance, created, **kwargs):
  if created:
    keyword = instance.keyword
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    live_search_type(keyword, keyword_and, keyword_or, keyword_nor, limit)    

email = os.environ.get("EMAIL_TWEET")
password = os.environ.get("PASSWORD_TWEET")
api_route = os.environ.get("API_ROUTE")

def basic_search_type(keyword,  keyword_and, keyword_or, keyword_nor, limit):
    basic_search_url = api_route + '/search/twitter/7-day'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(basic_search(keyword, keyword_and, keyword_or, keyword_nor, limit, auth_token, basic_search_url))["resourceId"]
    time.sleep(10)
    search.delay(report_id, auth_token)

def historical_search_type(keyword, keyword_and, keyword_or, keyword_nor, limit, start_date, end_date):
    historical_search_url = api_route + '/search/twitter/historical'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(historical_search(keyword, keyword_and, keyword_or, keyword_nor, limit, start_date, end_date, auth_token, historical_search_url))["resourceId"]
    time.sleep(10)
    search.delay(report_id, auth_token)   

def live_search_type(keyword, keyword_and, keyword_or, keyword_nor, limit):
    live_search_url = api_route + '/search/twitter/live'
    auth_token = json.loads(login(email, password))['authToken'] 
    live_search(keyword, keyword_and, keyword_or, keyword_nor, limit, auth_token, live_search_url)

def add_post_to_database(data_tweets):
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
                'creation_date': datetime.fromtimestamp(tweet['createdAt']), 
                'date': datetime.fromtimestamp(tweet['createdAt']), 
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
                'sentiment': tweet['sentiment']['vote'], 
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

@shared_task
def search(report_id, auth_token):
    while json.loads(get_report_state(report_id, auth_token))['status'] == "waiting":
        print(json.loads(get_report_state(report_id, auth_token))['status'])
    if json.loads(get_report_state(report_id, auth_token))['status'] == "generated":
        data_tweets = json.loads(get_publications(report_id, auth_token))
        add_post_to_database(data_tweets['data'])
        pagination = data_tweets['pagination']['nextResults']
        while pagination != None:
            data_tweets = json.loads(get_publications_next_page(report_id, auth_token, pagination))
            add_post_to_database(data_tweets['data'])
            pagination = data_tweets['pagination']['nextResults']
    else:
       print('Report not generated') 
       print(json.loads(get_report_state(report_id, auth_token))['status'])
    delete_report(auth_token, report_id)

class TweetBinderUserTracker(models.Model):
   user_alias = models.CharField(max_length=100, blank=False, null=False)
   start_date = models.DateTimeField(blank=True, null=True)
   end_date = models.DateTimeField(blank=True, null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)
   account_analysis_project = models.ForeignKey(ProjectAccountAnalysis, blank=True, null=True, on_delete=models.CASCADE)

   def __str__(self):
      return self.user_alias

class TweetBinderUserTrackerAnalysis(models.Model):
  user_alias = models.ForeignKey(TweetBinderUserTracker,blank=True,null=True,on_delete=models.CASCADE)
  tracker_id_start = models.CharField(max_length=100, blank=True, null=True)
  tracker_id_end = models.CharField(max_length=100, blank=True, null=True)
  mentions_start = models.CharField(max_length=100, blank=True, null=True)
  mentions_end = models.CharField(max_length=100, blank=True, null=True)
  tweets_start = models.CharField(max_length=100, blank=True, null=True)
  tweets_end = models.CharField(max_length=100, blank=True, null=True)
  deleted_start = models.CharField(max_length=100, blank=True, null=True)
  deleted_end = models.CharField(max_length=100, blank=True, null=True)
  originals_start = models.CharField(max_length=100, blank=True, null=True)
  originals_end = models.CharField(max_length=100, blank=True, null=True)
  retweet_statuses_start = models.CharField(max_length=100, blank=True, null=True)
  retweet_statuses_end = models.CharField(max_length=100, blank=True, null=True)
  retweets_start = models.CharField(max_length=100, blank=True, null=True)
  retweets_end = models.CharField(max_length=100, blank=True, null=True)
  favorites_start = models.CharField(max_length=100, blank=True, null=True)
  favorites_end = models.CharField(max_length=100, blank=True, null=True)
  followers_start = models.CharField(max_length=100, blank=True, null=True)
  followers_end = models.CharField(max_length=100, blank=True, null=True)
  following_start = models.CharField(max_length=100, blank=True, null=True)
  following_end = models.CharField(max_length=100, blank=True, null=True)
  lists_start = models.CharField(max_length=100, blank=True, null=True)
  lists_end = models.CharField(max_length=100, blank=True, null=True)
  followers_following_start = models.CharField(max_length=100, blank=True, null=True)
  followers_following_end = models.CharField(max_length=100, blank=True, null=True)
  user_value_start = models.CharField(max_length=100, blank=True, null=True)
  user_value_end = models.CharField(max_length=100, blank=True, null=True)
  engagement_value_start = models.CharField(max_length=100, blank=True, null=True)
  engagement_value_end = models.CharField(max_length=100, blank=True, null=True)
  global_score_start = models.CharField(max_length=100, blank=True, null=True)
  global_score_end = models.CharField(max_length=100, blank=True, null=True)
  created_at_start = models.DateTimeField(auto_now_add=True)
  created_at_end = models.DateTimeField(auto_now_add=True)
  updated_at_start = models.DateTimeField(auto_now_add=True)
  updated_at_start = models.DateTimeField(auto_now_add=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.user_alias.user_alias

@receiver(post_save, sender=TweetBinderUserTracker)
def greate_user_tracker_project(sender, instance, created, **kwargs):
  if created:
    user_alias = instance.user_alias
    start_date = instance.start_date
    end_date = instance.end_date
    url = api_route + '/user-trackers/multi'
    auth_token = json.loads(login(email, password))['authToken'] 
    tracker_id = json.loads(greate_user_tracker(user_alias, auth_token, url))['ok'][0]['resourceId']
    time.sleep(10)
    data_account = json.loads(get_user_tracker_stats(tracker_id, int(datetime.timestamp(start_date)), int(datetime.timestamp(end_date)), auth_token))
    add_data_account_to_database(data_account, instance)
    stop_user_trackers(api_route + '/user-trackers/delete', auth_token, tracker_id)

def add_data_account_to_database(data_account, instance):
  new_data = {  
                'user_alias': instance,
                'tracker_id_start': data_account[0]["_id"],
                'tracker_id_end': data_account[1]["_id"],
                'mentions_start': data_account[0]["mentions"],
                'mentions_end': data_account[1]["mentions"],
                'tweets_start': data_account[0]["tweets"],
                'tweets_end': data_account[1]["tweets"],
                'deleted_start': data_account[0]["deleted"],
                'deleted_end': data_account[1]["deleted"],
                'originals_start': data_account[0]["originals"],
                'originals_end': data_account[1]["originals"],
                'retweet_statuses_start': data_account[0]["retweetStatuses"],
                'retweet_statuses_end': data_account[1]["retweetStatuses"],
                'retweets_start': data_account[0]["retweets"],
                'retweets_end': data_account[1]["retweets"],
                'favorites_start': data_account[0]["favorites"],
                'favorites_end': data_account[1]["favorites"], 
                'followers_start': data_account[0]["followers"],
                'followers_end': data_account[1]["followers"],
                'following_start': data_account[0]["following"],
                'following_end': data_account[1]["following"],
                'lists_start': data_account[0]["lists"],
                'lists_end': data_account[1]["lists"],
                'followers_following_start': data_account[0]["followersFollowing"],
                'followers_following_end': data_account[1]["followersFollowing"],
                'user_value_start': data_account[0]["userValue"],
                'user_value_end': data_account[1]["userValue"],
                'engagement_value_start': data_account[0]["engagementValue"],
                'engagement_value_end': data_account[1]["engagementValue"],
                'global_score_start': data_account[0]["globalScore"],
                'global_score_end': data_account[1]["globalScore"],
                'created_at_start': data_account[0]["createdAt"],
                'created_at_end': data_account[1]["createdAt"],
                'updated_at_start': data_account[0]["updatedAt"],
                'updated_at_start': data_account[1]["updatedAt"],
            }
  TweetBinderUserTrackerAnalysis.objects.create(**new_data)
