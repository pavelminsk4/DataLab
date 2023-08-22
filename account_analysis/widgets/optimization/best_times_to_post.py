from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from account_analysis.models import AccountAnalysisWidgetDescription
from django.db.models import Sum, F
from django.http import JsonResponse

def best_times_to_post(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    widget = AccountAnalysisWidgetDescription.objects.get(id=widget_pk)
    results = [{'weekday': '', 'time': '', 'engagements': 0, 'likes': 0, 'retweets': 0, 'replies': 0} for i in range(1, 8)]
    for hour in range(0, 24):
        for day_of_week in range(1, 8):
            engagements, likes, retweets, replies, count_posts = 0, 0, 0, 0, 0
            posts_of_day = posts.filter(date__week_day=day_of_week).filter(date__hour=hour)
            first_post = posts_of_day.first()
            if posts_of_day:
                for post in posts_of_day:
                    count_posts += 1
                    engagements += (post.count_favorites + post.count_totalretweets)
                    likes += post.count_favorites
                    retweets += post.count_retweets
                    replies += post.count_replies
                results[day_of_week-1]['weekday'] = first_post.date.strftime('%A')
                results[day_of_week-1]['time'] = posts_of_day.first().date.strftime('%-I %p')
                results[day_of_week-1]['engagements'] = engagements/count_posts
                results[day_of_week-1]['likes'] = likes
                results[day_of_week-1]['retweets'] = retweets
                results[day_of_week-1]['replies'] = replies
    results = sorted(results, key=lambda engagements: engagements['engagements'], reverse=True)[:widget.top_counts]
    return JsonResponse(results, safe=False)
