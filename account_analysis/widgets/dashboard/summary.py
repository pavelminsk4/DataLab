from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from tweet_binder.models import TweetBinderPost
from django.db.models import Sum, F
from django.http import JsonResponse

def account_analysis_summary(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    user_post = TweetBinderPost.objects.filter(user_alias=project.profile_handle).last()
    posts_count = posts.count()
    engagements = posts.aggregate(count=Sum(F('count_favorites') + F('count_totalretweets')))['count']
    res = {
      'user_name': user_post.user_name,
      'user_picture': user_post.user_picture,
      'user_alias': user_post.user_alias,
      'user_bio': user_post.user_bio,
      'user_value': user_post.user_value,
      'verified': user_post.user_verified,
      'location': user_post.user_location,
      'stats' : {
        'total_followers': user_post.user_followers,
        'total_following': user_post.user_following,
        'total_tweets': posts_count,
        'tweets_this_period': posts_count,
        'engagements': engagements,
        'avg_likes_per_post': float(posts.aggregate(count=Sum('count_favorites'))['count']) / posts_count if posts_count else 0,
        'avg_retweets_per_post': float(posts.aggregate(count=Sum('count_totalretweets'))['count']) / posts_count if posts_count else 0,
        'avg_engagement_rate': engagements / posts_count if posts_count else 0,
      }
    }
    return JsonResponse(res, safe=False)
