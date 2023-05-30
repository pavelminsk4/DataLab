from account_analysis.widgets.optimization.average_engagements_by_day import calculate
from account_analysis.widgets.filter_for_posts import posts_aggregator
from account_analysis.models import ProjectAccountAnalysis

def average_engagements_by_day_for_mentions(pk, widget_pk):
    project = ProjectAccountAnalysis.objects.get(id=pk)
    posts = posts_aggregator(project)
    posts = posts.filter(text__icontains=f'@{project.profile_handle}')
    return calculate(posts)
