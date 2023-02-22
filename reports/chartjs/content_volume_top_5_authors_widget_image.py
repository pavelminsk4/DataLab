from widgets.common_widget.content_volume_top_5_source_widget import *
from project.models import *
from quickchart import QuickChart
from .services.algorithm_for_count_content_volume_widgets import algorithm_for_count_volume_widgets

def create_content_volume_top_5_authors_widget_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  smpl_freq = proj.widgets_list_2.content_volume_top_5_source_widget.aggregation_period
  top_authors = list(map(lambda x: x['entry_author'], list(posts.values('entry_author').annotate(author_count=Count('entry_author')).order_by('-author_count')[:10])))
  results = [{author: list(posts.filter(entry_author=author).annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date"))} for author in top_authors]
  res, colors = algorithm_for_count_volume_widgets(top_authors, results)
  authors = [[author for author in res[i]] for i in range(len(res))]           
  labels_list = [res[0][authors[0][0]][i]['date'][:10] for i in range(len(res[0][authors[0][0]]))]
  data_list = [res[i][authors[i][0]] for i in range(len(authors))]
  data = []
  for i in range(len(res)):
    data.append([data_list[i][j]['post_count'] for j in range(len(labels_list))])
  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  datasets = []
  for i in range(len(authors)):
    datasets.append({
                        'label': authors[i],
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
  qc.to_file('tmp/content_volume_top_5_authors_widget.png')
