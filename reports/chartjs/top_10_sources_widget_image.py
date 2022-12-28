from widgets.common_widget.top_10_brands_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_top_10_widgets import algorithm_for_count_top_10_widgets

def create_top_10_sources_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  results = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:10]
  qc = algorithm_for_count_top_10_widgets(proj, results, 'feedlink__source1', 'brand_count')
  qc.to_file('tmp/top_10_sources_widget.png')
