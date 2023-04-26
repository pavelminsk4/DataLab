from account_analysis.widgets.filter_for_posts import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse

def account_analysis_summary(pk, widget_pk):
  project = ProjectAccountAnalysis.objects.get(id=pk)
  account_analysis_tracker = TweetBinderUserTracker.objects.get(account_analysis_project=project)
  user_tracker_analysis = TweetBinderUserTracker.objects.create(user_alias=project.profile_handle, start_date=project.start_search_date, end_date=project.end_search_date, account_analysis_project=project)
  posts = posts_aggregator(project)
  res = {
    'user_name': posts.filter(user_alias=project.profile_handle).first().user_name,
    'user_alias': project.profile_handle,
    'user_bio':  posts.filter(user_alias=project.profile_handle).first().user_bio,
    'verified': posts.filter(user_alias=project.profile_handle).first().user_verified,
    'location': posts.filter(user_alias=project.profile_handle).first().user_location,
    'user_value': posts.filter(user_alias=project.profile_handle).first().user_value,
    'total_followers': user_tracker_analysis.followers_end,
    'total_following': user_tracker_analysis.following_end,
    'total_tweets': user_tracker_analysis.tweets_end,
    'tweets_this_period': float(user_tracker_analysis.tweets_end) - float(user_tracker_analysis.tweets_start),
    'enagagements': user_tracker_analysis.engagement_value_end,
    'avg_likes_per_post': (float(user_tracker_analysis.favorites_end) - float(user_tracker_analysis.favorites_start))/(float(user_tracker_analysis.tweets_end) - float(user_tracker_analysis.tweets_start)),
    'avg_retweets_per_post':(float(user_tracker_analysis.retweets_end) - float(user_tracker_analysis.retweets_start))/(float(user_tracker_analysis.tweets_end) - float(user_tracker_analysis.tweets_start)),
    'avg_engagement_rate': (float(user_tracker_analysis.engagement_value_end) - float(user_tracker_analysis.engagement_value_start))/(float(user_tracker_analysis.tweets_end) - float(user_tracker_analysis.tweets_start)),
    }
  return JsonResponse(res, safe=False)
