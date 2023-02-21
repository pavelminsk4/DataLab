from widgets.common_widget.sentiment_top_10_languages_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_sentiment_top_10_widgets import algorithm_for_count_sentiment_top_10_widgets

def create_sentiment_top_10_languages_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  top_languages = posts.values('feed_language__language').annotate(brand_count=Count('feed_language__language')).order_by('-brand_count').values_list('feed_language__language', flat=True)[:10]
  results = {language: list(posts.filter(feed_language__language=language).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for language in top_languages}
  qc = algorithm_for_count_sentiment_top_10_widgets(results, top_languages)
  qc.to_file('tmp/sentiment_top_10_languages_widget.png')
