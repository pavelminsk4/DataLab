from widgets.common_widget.project_posts_filter import project_posts_filter
from django.forms.models import model_to_dict
from django.http import JsonResponse
import collections
import itertools
from common.stopwords import STOPWORDS


def top_keywords(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = post_agg_top_keywords(posts)
    return JsonResponse(res, safe=False)

def top_keywords_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': post_agg_top_keywords(posts),
        'widget': {'top_keywords': model_to_dict(widget)},
        'module_name': 'Online'
    }

def post_agg_top_keywords(posts):
    words = list(itertools.chain(
      *[list(set(post.entry_summary.lower().split())) for post in posts]))
    tokens = sorted(collections.Counter(words).items(), key=lambda x:x[1], reverse=True)
    keywords = []
    for token in tokens:
        if (token[0] not in STOPWORDS and token[0].isalpha()):
            keywords.append(token)
        if (len(keywords) == 20):
            break
    keywords = dict(keywords)
    return [{'key' : kw, 'value' : keywords[kw]/len(posts)} for kw in keywords]

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = post_agg_top_keywords(posts)
    fields = ['Keyword', 'Value']
    rows = [[elem['key'], elem['value']] for elem in result]
    return fields, rows
