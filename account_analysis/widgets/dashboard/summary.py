from account_analysis.widgets.filter_for_posts import posts_aggregator
from account_analysis.models import ProjectAccountAnalysis
from tweet_binder.models import TweetBinderPost
from django.db.models import Sum, F
from django.http import JsonResponse

def account_analysis_summary(pk, widget_pk):
  project = ProjectAccountAnalysis.objects.get(id=pk)
  posts = posts_aggregator(project)
  project.count_posts = posts.count()
  project.followers = posts.last().user_followers
  user_post = TweetBinderPost.objects.filter(user_alias=project.profile_handle).last()
  user_posts = posts.filter(user_alias=project.profile_handle)
  engagements = posts.aggregate(count=Sum(F('count_favorites') + F('count_retweets')))['count']
  res = {
    'user_name': user_post.user_name,
    'user_picture': user_post.user_picture,
    'user_alias': project.profile_handle,
    'user_bio': user_post.user_bio,
    'user_value': user_post.user_value,
    'verified': user_post.user_verified,
    'location': user_post.user_location,
    'stats' : {
      'total_followers': user_posts.last().user_followers,
      'total_following': user_posts.last().user_following,
      'total_tweets': user_posts.count(),
      'tweets_this_period': user_posts.count(),
      'engagements': engagements,
      'avg_likes_per_post': float(user_posts.aggregate(count=Sum('count_favorites'))['count']) / user_posts.count() if user_posts.count() else 0,
      'avg_retweets_per_post': float(user_posts.aggregate(count=Sum('count_retweets'))['count']) / user_posts.count() if user_posts.count() else 0,
      'avg_engagement_rate': engagements / user_posts.count() if posts.count() else 0,
    }
  }
  return JsonResponse(res, safe=False)
