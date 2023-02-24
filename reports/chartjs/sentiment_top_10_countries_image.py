from widgets.common_widget.sentiment_top_10_countries_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_sentiment_top_10_widgets import algorithm_for_count_sentiment_top_10_widgets

def create_sentiment_top_10_countries_wid_image(project_id, widget_pk):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  top_countries = posts.values('feedlink__country').annotate(brand_count=Count('feedlink__country')).order_by('-brand_count').values_list('feedlink__country', flat=True)[:10]
  results = {country: list(posts.filter(feedlink__country=country).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for country in top_countries}
  qc = algorithm_for_count_sentiment_top_10_widgets(results, top_countries)
  qc.to_file('tmp/sentiment_top_10_countries_widget.png')
