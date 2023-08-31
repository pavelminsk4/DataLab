from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse


def optimal_post_time(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    return calculation(posts)

def calculation(posts):    
    res = [[{'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0} for i in range(24)] for d in range(1, 8)]
    for post in posts:
        day = post.date.weekday()
        hour = post.date.hour
        res[day][hour]['engagements'] += (post.count_favorites + post.count_totalretweets)
        res[day][hour]['likes'] += post.count_favorites
        res[day][hour]['retweets'] += post.count_totalretweets
        res[day][hour]['tweets'] += 1
    results = {
           'Saturday': res[6],
           'Friday': res[5],
           'Thursday': res[4],
           'Wednesday': res[3],
           'Tuesday': res[2],
           'Monday': res[1],
           'Sunday': res[0]
           }
    return JsonResponse(results, safe=False)
