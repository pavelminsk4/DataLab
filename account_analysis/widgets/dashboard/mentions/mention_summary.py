from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from tweet_binder.models import TweetBinderPost
from django.db.models import Sum
from django.http import JsonResponse

def mention_summary(pk, widget_pk):
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    user_post = TweetBinderPost.objects.filter(user_alias=project.profile_handle).last()
    positive, negative, neutral = 0, 0, 0
    for post in posts:
        if post.sentiment == 'positive':
            positive += 1
        elif post.sentiment == 'negative':
            negative += 1
        elif post.sentiment == 'neutral':
            neutral += 1 
    res = {
        'user_name': user_post.user_name,
        'user_picture': user_post.user_picture,
        'user_alias': project.profile_handle,
        'user_bio': user_post.user_bio,
        'user_value': user_post.user_value,
        'verified': user_post.user_verified,
        'location': user_post.user_location,
        'stats': {
            'mention': posts.count(),
            'language': posts.values('language').distinct().count(),
            'countries': posts.values('user_location').distinct().count(),
            'authors': posts.values('user_alias').distinct().count(),
            'neutral': neutral,
            'negative': negative,
            'positive': positive,
            'potential_rates': posts.aggregate(value=Sum('user_value'))['value'],
        }
    }
    return JsonResponse(res, safe=False)
