from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse


def optimal_post_time(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    return calculation(posts)

def calculation(posts):    
    res = [[{'engagements': 0, 'likes': 0, 'retweets': 0, 'tweets': 0} for i in range(24)] for d in range(1, 8)]
    for hour in range(0, 24):
        posts_of_hour = posts.filter(date__hour=hour)
        for day_of_week in range(1, 8):
            engagements, likes, retweets, count_posts = 0, 0, 0, 0
            posts_of_day = posts_of_hour.filter(date__week_day=day_of_week)
            if len(posts_of_day) > 0:
                for post in list(posts_of_day):
                    count_posts += 1
                    engagements += (post.count_favorites + post.count_totalretweets)
                    likes += post.count_favorites
                    retweets += post.count_totalretweets
                res[day_of_week-1][hour]['engagements'] = engagements/count_posts if count_posts else 0
                res[day_of_week-1][hour]['likes'] = likes
                res[day_of_week-1][hour]['retweets'] = retweets
                res[day_of_week-1][hour]['tweets'] = count_posts
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
