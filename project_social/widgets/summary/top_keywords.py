from project_social.widgets.project_posts_filter import project_posts_filter
from common.social_keywords import get_keywords
from django.forms.models import model_to_dict
from django.http import JsonResponse

def top_keywords(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    res = get_keywords(posts)
    return JsonResponse(res, safe = False)

def top_keywords_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': get_keywords(posts),
        'widget': {'top_keywords': model_to_dict(widget)},
        'module_name': 'Social'
    }

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = get_keywords(posts)
    fields = ['Keyword', 'Value']
    rows = [[elem['key'], elem['value']] for elem in result]
    return fields, rows
