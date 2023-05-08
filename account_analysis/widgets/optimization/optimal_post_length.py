from account_analysis.widgets.filter_for_posts import posts_aggregator
from account_analysis.models import ProjectAccountAnalysis
from django.db.models import Sum, F, Q
from django.http import JsonResponse


def optimal_post_length(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts_from_0_to_45 = posts.filter(count_textlength__lte=45)
    posts_from_46_to_90 = posts.filter(Q(count_textlength__gte=46) & Q(count_textlength__lte=90))
    posts_from_91_to_140 = posts.filter(Q(count_textlength__gte=91) & Q(count_textlength__lte=140))
    posts_from_140 = posts.filter(count_textlength__gte=140)
    engagement = Sum(F('count_favorites') + F('count_retweets'))
    res = {
            'from 0 to 45': posts_from_0_to_45.aggregate(engagement=engagement)['engagement']/posts_from_0_to_45.count() if posts_from_0_to_45.count() else 0,
            'from 46 to 90': posts_from_46_to_90.aggregate(engagement=engagement)['engagement']/posts_from_46_to_90.count() if posts_from_46_to_90.count() else 0,
            'from 91 to 140': posts_from_91_to_140.aggregate(engagement=engagement)['engagement']/posts_from_91_to_140.count() if posts_from_91_to_140.count() else 0,
            'from 140': posts_from_140.aggregate(engagement=engagement)['engagement']/posts_from_140.count() if posts_from_140.count() else 0
          }
    return JsonResponse(res, safe=False)
