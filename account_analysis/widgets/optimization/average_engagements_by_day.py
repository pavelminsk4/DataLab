from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse


def average_engagements_by_day(pk, widget_pk):
    posts, project = filter_for_account_posts(pk, widget_pk)
    return calculate(posts)

def calculate(posts):
    engagements_sunday, engagements_monday, engagements_tuesday, engagements_wednesday, engagements_thursday, engagements_friday, engagements_saturday = 0,0,0,0,0,0,0
    posts_sunday, posts_monday, posts_tuesday, posts_wednesday, posts_thursday, posts_friday, posts_saturday = 0,0,0,0,0,0,0
    for post in posts:
        date = post.date
        if date.weekday() == 1:
            posts_sunday += 1
            engagements_sunday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 2:
            posts_monday += 1
            engagements_monday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 3:
            posts_tuesday += 1
            engagements_tuesday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 4:
            posts_wednesday += 1
            engagements_wednesday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 5:
            posts_thursday += 1
            engagements_thursday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 6:
            posts_friday += 1
            engagements_friday += (post.count_favorites + post.count_totalretweets)
        elif date.weekday() == 0:
            posts_saturday += 1
            engagements_saturday += (post.count_favorites + post.count_totalretweets)
    res = {'Monday': engagements_monday/posts_monday if posts_monday else 0,
           'Tuesday': engagements_tuesday/posts_tuesday if posts_tuesday else 0,
           'Wednesday': engagements_wednesday/posts_wednesday if posts_wednesday else 0,
           'Thursday': engagements_thursday/posts_thursday if posts_thursday else 0,
           'Friday': engagements_friday/posts_friday if posts_friday else 0,
           'Saturday': engagements_saturday/posts_saturday if posts_saturday else 0,
           'Sunday': engagements_sunday/posts_sunday if posts_sunday else 0}
    return JsonResponse(res, safe=False)
