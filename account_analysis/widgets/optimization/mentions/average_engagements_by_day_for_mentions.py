from account_analysis.widgets.optimization.average_engagements_by_day import calculate
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from account_analysis.models import ProjectAccountAnalysis
from django.http import JsonResponse

def average_engagements_by_day_for_mentions(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    return JsonResponse(calculate(posts), safe=False)

def to_csv(request, pk, widget_pk):
    posts, project, widget = filter_for_mentions_posts(pk, widget_pk)
    result = calculate(posts)
    fields = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    rows = [[result['Monday'], result['Tuesday'], result['Wednesday'], result['Thursday'], result['Friday'], result['Saturday'], result['Sunday']]]
    return fields, rows
