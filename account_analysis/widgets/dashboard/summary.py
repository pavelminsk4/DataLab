from account_analysis.widgets.filter_for_posts import *
from account_analysis.models import *
from tweet_binder.models import *
from django.http import JsonResponse

def account_analysis_summary(pk, widget_pk):
  project = ProjectAccountAnalysis.objects.get(id=pk)
  user_tracker = TweetBinderUserTracker.objects.create(user_alias=project.profile_handle, start_date=project.start_search_date, end_date=project.end_search_date, account_analysis_project=project)
  posts = posts_aggregator(project)
  project.count_posts = posts.count()
  user_tracker_analysis = TweetBinderUserTrackerAnalysis.objects.get(user_alias=user_tracker.pk)
  project.followers = user_tracker_analysis.followers_end
  user_post = TweetBinderPost.objects.filter(user_alias=project.profile_handle).last()
  difference_tweets = float(user_tracker_analysis.tweets_end) - float(user_tracker_analysis.tweets_start)
  res = {
    'user_name': user_post.user_name,
    'user_alias': project.profile_handle,
    'user_bio': user_post.user_bio,
    'verified': user_post.user_verified,
    'location': user_post.user_location,
    'user_value': user_post.user_value,
    'total_followers': user_tracker_analysis.followers_end,
    'total_following': user_tracker_analysis.following_end,
    'total_tweets': user_tracker_analysis.tweets_end,
    'tweets_this_period': difference_tweets,
    'engagements': user_tracker_analysis.engagement_value_end,
    'avg_likes_per_post': (float(user_tracker_analysis.favorites_end) - float(user_tracker_analysis.favorites_start)) / difference_tweets if difference_tweets else 0,
    'avg_retweets_per_post':(float(user_tracker_analysis.retweets_end) - float(user_tracker_analysis.retweets_start))/ difference_tweets if difference_tweets else 0, 
    'avg_engagement_rate': (float(user_tracker_analysis.engagement_value_end) - float(user_tracker_analysis.engagement_value_start)) / difference_tweets if difference_tweets else 0,
    }
  return JsonResponse(res, safe=False)
