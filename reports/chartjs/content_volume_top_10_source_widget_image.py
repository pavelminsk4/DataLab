from widgets.common_widget.content_volume_top_10_source_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_content_volume_widgets import algorithm_for_count_volume_widgets

def create_content_volume_top_10_source_widget_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  smpl_freq = proj.widgets_list_2.content_volume_top_10_source_widget.aggregation_period
  top_brands = list(map(lambda x: x['feedlink__source1'], list(posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:10])))
  results = [{source: list(posts.filter(feedlink__source1=source).annotate(date=Trunc('entry_published', smpl_freq)).values('date').annotate(created_count=Count('id')).order_by('date'))} for source in top_brands]
  res, colors = algorithm_for_count_volume_widgets(top_brands, results)
  sources = [[source for source in res[i]] for i in range(len(res))]           
  labels_list = [res[0][sources[0][0]][i]['date'][:10] for i in range(len(res[0][sources[0][0]]))]
  data_list = [res[i][sources[i][0]] for i in range(len(sources))]
  data = []
  for i in range(len(res)):
    data.append([data_list[i][j]['post_count'] for j in range(len(labels_list))])
  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  datasets = []
  for i in range(len(sources)):
    datasets.append({
                        'label': sources[i],
                        'data': data[i],
                        'lineTension': 0.4,
                        'borderColor': colors[i],
                        'backgroundColor': 'transparent',
                    },)
  qc.config = {
    'type': 'line',
    'data': {
        'labels': labels_list,
        'datasets': datasets
      }
  }
  qc.to_file('tmp/content_volume_top_10_source_widget.png')
