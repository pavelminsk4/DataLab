from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse


def optimal_post_time(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    return JsonResponse(calculation(posts), safe=False)

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
           'Saturday': res[5],
           'Friday': res[4],
           'Thursday': res[3],
           'Wednesday': res[2],
           'Tuesday': res[1],
           'Monday': res[0],
           'Sunday': res[6]
           }
    return results

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = calculation(posts)
    fields = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = ['0 AM', '1 AM', '2 AM', '3 AM', '4 AM', '5 AM', '6 AM', '7 AM', '8 AM', '9 AM', '10 AM', '11 AM', '12 AM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM', '9 PM', '10 PM', '11 PM', '12 PM']
    rows = []
    for time in range(0, 24):
        row = []
        row.append(times[time])
        for day in fields[1:]:
            row.append(result[day][time]['engagements'])
        rows.append(row)
    return fields, rows
