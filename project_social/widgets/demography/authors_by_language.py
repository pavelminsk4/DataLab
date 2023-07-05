from project_social.widgets.filters_for_widgets import post_agregator_with_dimensions, post_agregetor_for_each_widget
from project_social.models import SocialWidgetDescription
from common.descending_sort import descending_sort
from project_social.models import ProjectSocial
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.db.models import Count


def calculate(posts, widget):
    top_languages = [i['language'] for i in posts.values('language').annotate(author_count=Count('user_alias', distinct=True)).order_by('-author_count')[:5]]
    results = []
    for language in top_languages:
        top_authors = posts.filter(language=language).values('user_alias').annotate(posts_count=Count('id')).order_by('-posts_count')[:5]
        authors_posts = {author['user_alias']: author['posts_count'] for author in top_authors}
        results.append({language: descending_sort(authors_posts)})
    return results
    
def authors_by_language(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return JsonResponse(calculate(posts, widget), safe = False)

def authors_by_language_report(pk, widget_pk):
    project = ProjectSocial.objects.get(id=pk)
    posts = post_agregator_with_dimensions(project)
    widget = SocialWidgetDescription.objects.get(id=widget_pk)
    posts = post_agregetor_for_each_widget(widget, posts)
    return {
        'data': calculate(posts, widget),
        'widget': {'authors_by_language': model_to_dict(widget)}
    }
