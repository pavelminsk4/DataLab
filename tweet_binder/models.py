
from account_analysis.models import ProjectAccountAnalysis
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from project.models import Speech
from transformers import pipeline
from langcodes import Language
from celery import shared_task
from django.db import models

from .services.get_report_new_tweets import get_report_new_tweets, get_report_new_tweets_next_page
from .services.get_publications import get_publications, get_publications_next_page
from .services.get_user_tracker_stats import get_user_tracker_stats
from .services.greate_user_tracker import greate_user_tracker
from .services.stop_user_trackers import stop_user_trackers
from .services.enterprise_search import enterprise_search
from .services.get_report_state import get_report_state
from .services.delete_report import delete_report
from .services.basic_search import basic_search
from .services.live_search import live_search
from .services.login import login

from datetime import datetime
import time
import json
import os

from django.contrib.postgres.indexes import GinIndex, OpClass
from django.db.models.functions import Upper


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
    imp_sentiment = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.post_id
  
    class Meta:
        indexes = [
            models.Index(fields=['date',]),
            GinIndex(
                OpClass(Upper('text'), name='gin_trgm_ops'),
                name='tb_text_gin_index',
              ),
            GinIndex(
                OpClass(Upper('user_name'), name='gin_trgm_ops'),
                name='tb_user_name_gin_index',
              ),
            GinIndex(
                OpClass(Upper('user_alias'), name='gin_trgm_ops'),
                name='tb_user_alias_gin_index',
              )
          ]  


class TypesOfSearch(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  limit = models.IntegerField(blank=True, null=True, default=10)
  keyword_and = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords AND')
  keyword_or = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords OR')
  keyword_nor = ArrayField(models.CharField(max_length=100), blank=True, null=True, verbose_name='Keywords excluded')

  
  class Meta:
    abstract = True

class EnterpriseSearchProject(TypesOfSearch):
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  
  def __str__(self):
      return self.title

@receiver(post_save, sender=EnterpriseSearchProject)
def create_enterprise_search_project(sender, instance, created, **kwargs):
  if created:
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    start_date = instance.start_date
    end_date = instance.end_date
    enterprise_search_type(keyword_and, keyword_or, keyword_nor, limit, start_date, end_date)

class BasicSearchProject(TypesOfSearch):

  def __str__(self):
      return self.title

@receiver(post_save, sender=BasicSearchProject)
def create_basic_search_project(sender, instance, created, **kwargs):
  if created:
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    basic_search_type(keyword_and, keyword_or, keyword_nor, limit)          

class LiveSearchProject(TypesOfSearch):
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)

  def __str__(self):
      return self.title

@receiver(post_save, sender=LiveSearchProject)
def create_live_search_project(sender, instance, created, **kwargs):
  if created:
    keyword_and = instance.keyword_and
    keyword_or = instance.keyword_or
    keyword_nor = instance.keyword_nor
    limit = instance.limit
    start_date = instance.start_date
    end_date = instance.end_date
    live_search_type(keyword_and, keyword_or, keyword_nor, limit, start_date, end_date)


class LiveReport(models.Model):
  report_id = models.CharField(max_length=40)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

@shared_task
def get_new_tweets_from_live_reports():
   auth_token = json.loads(login(email, password))['authToken'] 
   live_reports_for_check = LiveReport.objects.filter(end_date__gte=datetime.now())
   for report in live_reports_for_check:
      data_tweets = json.loads(get_report_new_tweets(report.report_id, auth_token, str(int(datetime.timestamp(report.start_date)))))
      if data_tweets.get('data'):
        add_post_to_database(data_tweets['data']) 
        pagination = data_tweets['pagination']['nextResults']
        while pagination != None:
            data_tweets = json.loads(get_report_new_tweets_next_page(report.report_id, auth_token, pagination, str(int(datetime.timestamp(report.start_date)))))
            add_post_to_database(data_tweets['data'])
            pagination = data_tweets['pagination']['nextResults']
      else:
         print('No new tweets found')
   

email = os.environ.get('EMAIL_TWEET')
password = os.environ.get('PASSWORD_TWEET')
api_route = os.environ.get('API_ROUTE')

def basic_search_type(keyword_and, keyword_or, keyword_nor, limit):
    basic_search_url = api_route + '/search/twitter/7-day'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(basic_search(keyword_and, keyword_or, keyword_nor, limit, auth_token, basic_search_url))['resourceId']
    time.sleep(10)
    search.delay(report_id, auth_token)

def enterprise_search_type(keyword_and, keyword_or, keyword_nor, limit, start_date, end_date):
    enterprise_search_url = api_route + '/search/twitter/enterprise/'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(enterprise_search(keyword_and, keyword_or, keyword_nor, limit, start_date, end_date, auth_token, enterprise_search_url))['resourceId']
    time.sleep(10)
    search.delay(report_id, auth_token)   

def live_search_type(keyword_and, keyword_or, keyword_nor, limit, start_date, end_date):
    live_search_url = api_route + '/search/twitter/live/'
    auth_token = json.loads(login(email, password))['authToken'] 
    report_id = json.loads(live_search(keyword_and, keyword_or, keyword_nor, limit, auth_token, live_search_url, start_date, end_date))['resourceId']
    time.sleep(5)
    try:
        LiveReport.objects.create(report_id=report_id, start_date=start_date, end_date=end_date)
    except:
        print('Live report not created')
        pass
    

def calculate_sentiment(text):
   model_path = 'cardiffnlp/twitter-xlm-roberta-base-sentiment'
   sentiment_task = pipeline('sentiment-analysis', model=model_path, tokenizer=model_path, max_length=512, truncation=True)
   return sentiment_task(text)[0]['label']

def add_language(language_code):
  title = Language.get(language_code).display_name()
  return Speech.objects.get_or_create(language=title)[0]

def add_post_to_database(data_tweets):
  tweets = []
  for tweet in data_tweets:
    new_tweet = {
                'post_id': tweet.get('_id'),
                'async_ops': tweet.get('asyncOps'),
                'binders': tweet.get('binders'),
                'count_textlength': int(tweet['counts'].get('textLength')),
                'count_sentiment': tweet['counts'].get('sentiment'),
                'count_retweets': tweet['counts'].get('retweets'),
                'count_totalretweets': tweet['counts'].get('totalRetweets'),
                'count_favorites': tweet['counts'].get('favorites'),
                'count_hashtags': tweet['counts'].get('hashtags'),
                'count_images': tweet['counts'].get('images'),
                'count_links': tweet['counts'].get('links'),
                'count_linksandimages': tweet['counts'].get('linksAndImages'), 
                'count_mentions': tweet['counts'].get('mentions'), 
                'count_originals': tweet['counts'].get('originals'), 
                'count_clears': tweet['counts'].get('clears'),
                'count_replies': tweet['counts'].get('replies'),
                'count_publicationscore': tweet['counts'].get('publicationScore'), 
                'count_uservalue': tweet['counts'].get('userValue'), 
                'count_tweetvalue': tweet['counts'].get('tweetValue'), 
                'createdat': tweet.get('createdAt'),
                'creation_date': datetime.fromtimestamp(tweet.get('createdAt')), 
                'date': datetime.fromtimestamp(tweet.get('createdAt')), 
                'favorites': tweet.get('favorites'), 
                'hashtags': tweet.get('hashtags'), 
                'images': tweet.get('images'), 
                'inreplyto': tweet.get('inReplyTo'),  
                'inreplytoid': tweet.get('inReplyToId'),  
                'language': add_language(tweet.get('lang')),  
                'links': tweet.get('links'),  
                'mentions': tweet.get('mentions'),  
                'locationString': tweet['rawLocation'].get('locationString'),  
                'retweets': tweet.get('retweets'),  
                'sentiment_vote': tweet['sentiment'].get('vote') if tweet['sentiment'].get('vote') != 'undefined' else 'neutral', 
                'sentiment': tweet['sentiment'].get('vote') if tweet['sentiment'].get('vote') != 'undefined' else 'neutral', 
                'source': tweet.get('source'),
                'text': tweet.get('text'),
                'type': tweet.get('type'),  
                'updatedat': tweet.get('updatedAt'),
                'user_id': tweet['user'].get('id'), 
                'user_name': tweet['user'].get('name'),
                'user_alias': tweet['user'].get('alias'),
                'user_picture': tweet['user'].get('picture'),
                'user_followers': tweet['user'].get('followers'),
                'user_following': tweet['user'].get('following'), 
                'user_verified': tweet['user'].get('verified'), 
                'user_bio': tweet['user'].get('bio'), 
                'user_age': tweet['user'].get('age'), 
                'user_counts_lists':tweet['user']['counts'].get('lists'), 
                'user_statuses': tweet['user']['counts'].get('statuses'), 
                'user_location': tweet['user'].get('location'),
                'user_gender': tweet['user'].get('gender'), 
                'user_value': tweet['user'].get('value'),
                'videos': tweet.get('videos'),
                'imp_sentiment': calculate_sentiment(tweet.get('text'))
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
    i = 0
    while json.loads(get_report_state(report_id, auth_token))['status'] != 'generated' and i < 100:
        i += 1
        print(json.loads(get_report_state(report_id, auth_token))['status'])
    if json.loads(get_report_state(report_id, auth_token))['status'] == 'generated':
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
  n = 1 if len(data_account) > 1 else 0
  new_data = {  
                'user_alias': instance,
                'tracker_id_start': data_account[0]['_id'],
                'tracker_id_end': data_account[n]['_id'],
                'mentions_start': data_account[0]['mentions'],
                'mentions_end': data_account[n]['mentions'],
                'tweets_start': data_account[0]['tweets'],
                'tweets_end': data_account[n]['tweets'],
                'deleted_start': data_account[0]['deleted'],
                'deleted_end': data_account[n]['deleted'],
                'originals_start': data_account[0]['originals'],
                'originals_end': data_account[n]['originals'],
                'retweet_statuses_start': data_account[0]['retweetStatuses'],
                'retweet_statuses_end': data_account[n]['retweetStatuses'],
                'retweets_start': data_account[0]['retweets'],
                'retweets_end': data_account[n]['retweets'],
                'favorites_start': data_account[0]['favorites'],
                'favorites_end': data_account[n]['favorites'], 
                'followers_start': data_account[0]['followers'],
                'followers_end': data_account[n]['followers'],
                'following_start': data_account[0]['following'],
                'following_end': data_account[n]['following'],
                'lists_start': data_account[0]['lists'],
                'lists_end': data_account[n]['lists'],
                'followers_following_start': data_account[0]['followersFollowing'],
                'followers_following_end': data_account[n]['followersFollowing'],
                'user_value_start': data_account[0]['userValue'],
                'user_value_end': data_account[n]['userValue'],
                'engagement_value_start': data_account[0]['engagementValue'],
                'engagement_value_end': data_account[n]['engagementValue'],
                'global_score_start': data_account[0]['globalScore'],
                'global_score_end': data_account[n]['globalScore'],
                'created_at_start': data_account[0]['createdAt'],
                'created_at_end': data_account[n]['createdAt'],
                'updated_at_start': data_account[0]['updatedAt'],
                'updated_at_start': data_account[n]['updatedAt'],
            }
  TweetBinderUserTrackerAnalysis.objects.create(**new_data)
