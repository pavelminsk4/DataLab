from account_analysis.widgets.optimization.average_engagements_by_day import calculate
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from account_analysis.models import ProjectAccountAnalysis

def average_engagements_by_day_for_mentions(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    return calculate(posts)
