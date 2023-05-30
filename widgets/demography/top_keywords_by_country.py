from widgets.models import WidgetDescription
from widgets.common_widget.filters_for_widgets import *
from project.models import Project
from django.http import JsonResponse
from collections import Counter
import itertools
from common.stopwords import STOPWORDS
from django.db.models import Count


def get_top_keywords_by_country(pk, widget_pk):
    project = Project.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = WidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    countries = posts.values('feedlink__country').annotate(count=Count('feedlink__country')).order_by('-count')[:5]
    res = list(map(lambda x: {x['feedlink__country']: get_keywords(posts.filter(feedlink__country=x['feedlink__country']))}, countries))
    return JsonResponse(res, safe=False)


def get_keywords(posts):
    words = list(itertools.chain(*[list(set(post.entry_summary.lower().split())) for post in posts]))
    tokens = sorted(Counter(words).items(), key=lambda x: x[1], reverse=True)
    keywords = []
    for token in tokens:
        if (token[0] not in STOPWORDS and token[0].isalpha()):
            keywords.append(token)
        if (len(keywords) == 10):
            break
    keywords = dict(keywords)
    return [{'key': kw, 'value': keywords[kw]/len(posts)} for kw in keywords]
