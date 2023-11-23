from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.db.models import Sum, F
from django.http import JsonResponse


def optimal_number_of_hashtags(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    return JsonResponse(calculate(posts), safe=False)

def calculate(posts):
    posts = posts.annotate(engagement=Sum(F('count_favorites') + F('count_totalretweets'))).values('engagement', 'hashtags').order_by('-engagement')
    count_zero, count_from_1_to_2, count_from_3_to_4, count_from_5 = 0, 0, 0, 0
    engagement_zero, engagement_from_1_to_2, engagement_from_3_to_4, engagement_from_5 = 0, 0, 0, 0
    for p in posts:
        if len(p['hashtags']) == 0:
            count_zero += 1
            engagement_zero += p['engagement']
        elif len(p['hashtags']) >= 1 and len(p['hashtags']) <= 2:
            count_from_1_to_2 += 1
            engagement_from_1_to_2 += p['engagement']
        elif len(p['hashtags']) >= 3 and len(p['hashtags']) <= 4:
            count_from_3_to_4 += 1
            engagement_from_3_to_4 += p['engagement']
        elif len(p['hashtags']) >= 5:
            count_from_5 += 1
            engagement_from_5 += p['engagement']

    res = {
            'frequency': {
                'count_zero': count_zero,
                'count_from_1_to_2': count_from_1_to_2,
                'count_from_3_to_4': count_from_3_to_4,
                'count_from_5': count_from_5,
            },
            'engagement': {
                '0 hashtags': engagement_zero,
                '1-2 hashtags': engagement_from_1_to_2,
                '3-4 hashtags': engagement_from_3_to_4,
                '5+ hashtags': engagement_from_5
            }
          }
    return res

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = calculate(posts)
    fields = ['0 hashtags', '1-2 hashtags', '3-4 hashtags', '5+ hashtags']
    rows = [[result['engagement']['0 hashtags'], result['engagement']['1-2 hashtags'], result['engagement']['3-4 hashtags'], result['engagement']['5+ hashtags']]]
    return fields, rows
