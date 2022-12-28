from widgets.common_widget.sentiment_top_10_authors_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_sentiment_top_10_widgets import algorithm_for_count_sentiment_top_10_widgets

def create_sentiment_top_10_authors_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  top_authors = posts.values('entry_author').annotate(brand_count=Count('entry_author')).order_by('-brand_count').values_list('entry_author', flat=True)[:10]
  results = {author: list(posts.filter(entry_author=author).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for author in top_authors}
  qc = algorithm_for_count_sentiment_top_10_widgets(results, top_authors)
  qc.to_file('tmp/sentiment_top_10_authors_widget.png')
