from widgets.common_widget.top_10_countries_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_top_10_widgets import algorithm_for_count_top_10_widgets

def create_top_10_countries_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:10]
  qc = algorithm_for_count_top_10_widgets(proj, results, 'feedlink__country', 'country_count')
  qc.to_file('tmp/top_10_countries_widget.png')
