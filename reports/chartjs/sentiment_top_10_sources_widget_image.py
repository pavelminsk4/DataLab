from widgets.common_widget.sentiment_top_sources import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_sentiment_top_10_widgets import algorithm_for_count_sentiment_top_10_widgets

def create_sentiment_top_10_sources_wid_image(project_id, widget_pk):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_sources = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count').values_list('feedlink__source1', flat=True)[:10]
  results = {source: list(posts.filter(feedlink__source1=source).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for source in top_sources}
  qc = algorithm_for_count_sentiment_top_10_widgets(results, top_sources)
  qc.to_file('tmp/sentiment_top_10_sources_widget.png')
