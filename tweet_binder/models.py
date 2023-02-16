from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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

class TweetBinderProject(models.Model):
  title = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  limit = models.IntegerField(blank=True, null=True, default=10)
  keyword = models.CharField(max_length=100, blank=False, null=False)
  start_date = models.DateTimeField(blank=True, null=True)
  end_date = models.DateTimeField(blank=True, null=True)
  
  BASIC_SEARCH = 'basic search'
  HISTORICAL_SEARCH = 'historical search'
  LIVE_SEARCH =  'live search'
 
  TYPE_SEARCH = (
    (BASIC_SEARCH, 'Basic search'),
    (HISTORICAL_SEARCH, 'Historical search'),
    (LIVE_SEARCH, 'Live search'),
  )
  
  search_type = models.CharField(max_length=30, choices=TYPE_SEARCH, blank=True, null=True, default=TYPE_SEARCH[0][1])

  def __str__(self):
      return self.title
