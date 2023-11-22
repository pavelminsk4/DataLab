from project_social.widgets.project_posts_filter import project_posts_filter
from common.descending_sort import descending_sort
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def authors_by_gender(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return JsonResponse(calculate_for_authors_by_gender(posts, widget.top_counts), safe=False)

def authors_by_gender_report(pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    return {
        'data': calculate_for_authors_by_gender(posts, widget.top_counts),
        'widget': {'authors_by_gender': model_to_dict(widget)},
        'module_name': 'Social'
    }

def calculate_for_authors_by_gender(posts, top_counts):
    genders = ['male', 'female', 'undefined']
    results = {}
    for gender in genders:
        top_authors = list(posts.filter(user_gender=gender).values('user_name').annotate(author_post=Count('id')).order_by('-author_post')[:top_counts])
        results[gender] = descending_sort({author['user_name']: author['author_post'] for author in top_authors})
    return results

def to_csv(request, pk, widget_pk):
    posts, widget = project_posts_filter(pk, widget_pk)
    result = calculate_for_authors_by_gender(posts, widget.top_counts)
    fields = ['Gender', 'Author', 'Count of posts']
    rows = []
    for sen in ['male', 'female', 'undefined']:
        for elem in result[sen]:
            rows.append([sen, elem[0], elem[1]])
    return fields, rows
