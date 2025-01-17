from account_analysis.widgets.filter_for_posts import filter_for_account_posts
from django.http import JsonResponse


def optimal_post_length(pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    results = calculate(posts)
    return JsonResponse(results, safe=False)

def calculate(posts):
    posts_from_0_to_45_engagement, posts_from_0_to_45_count = 0, 0
    posts_from_46_to_90_engagement, posts_from_46_to_90_count = 0, 0
    posts_from_91_to_140_engagement, posts_from_91_to_140_count = 0, 0
    posts_from_140_engagement, posts_from_140_count = 0, 0
    for post in posts:
        if post.count_textlength <= 45:
            posts_from_0_to_45_engagement += post.count_favorites + post.count_totalretweets
            posts_from_0_to_45_count += 1
        if post.count_textlength >= 46 and post.count_textlength <= 90:
            posts_from_46_to_90_engagement += post.count_favorites + post.count_totalretweets
            posts_from_46_to_90_count += 1
        if post.count_textlength >= 91 and post.count_textlength <= 140:
            posts_from_91_to_140_engagement += post.count_favorites + post.count_totalretweets
            posts_from_91_to_140_count += 1
        if post.count_textlength >= 141:
            posts_from_140_engagement += post.count_favorites + post.count_totalretweets
            posts_from_140_count += 1
    results = {
                'from 0 to 45': posts_from_0_to_45_engagement/posts_from_0_to_45_count if posts_from_0_to_45_count else 0,
                'from 46 to 90': posts_from_46_to_90_engagement/posts_from_46_to_90_count if posts_from_46_to_90_count else 0,
                'from 91 to 140': posts_from_91_to_140_engagement/posts_from_91_to_140_count if posts_from_91_to_140_count else 0,
                'from 140': posts_from_140_engagement/posts_from_140_count if posts_from_140_count else 0,
              }
    return results

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_account_posts(pk, widget_pk)
    result = calculate(posts)
    fields = ['from 0 to 45', 'from 46 to 90', 'from 91 to 140', 'from 140']
    rows = [[result['from 0 to 45'], result['from 46 to 90'], result['from 91 to 140'], result['from 140']]]
    return fields, rows
