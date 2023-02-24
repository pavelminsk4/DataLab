from widgets.common_widget.top_10_languages_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_top_10_widgets import algorithm_for_count_top_10_widgets

def create_top_10_languages_wid_image(project_id, widget_pk):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:10]
  qc = algorithm_for_count_top_10_widgets(proj, results, 'feed_language__language', 'language_count')
  qc.to_file('tmp/top_10_languages_widget.png')
