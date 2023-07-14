from account_analysis.widgets.optimization.optimal_post_time import calculation
from account_analysis.widgets.filter_for_posts import filter_for_mentions_posts
from account_analysis.models import ProjectAccountAnalysis

def audience_mention_time(pk, widget_pk):
    posts, project = filter_for_mentions_posts(pk, widget_pk)
    return calculation(posts)
