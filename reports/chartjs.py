from quickchart import QuickChart
from widgets.common_widget.volume_widget import *
from project.models import *

def prepare_widget_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  smpl_freq = 'day'
  posts_per_smpl_freq = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").annotate(created_count=Count('id')).order_by("date")
  res = list(posts_per_smpl_freq)
  labels = []
  data = []
  type = 'line'
  for each in res:
    labels.append(each['date'].strftime("%x"))
    data.append(each['created_count'])
  chart = QuickChart()
  chart.width = 900
  chart.height = 450
  chart.config = {
      "type": type,
      "data":{
          "labels": labels,
          "datasets": [
            {
              'label': proj.title ,
              "data": data,
              'lineTension': 0.4,
            },
          ],
        },
      'options': {
        'legend': {
          'position': 'bottom',
          },
        'scales': {
            'xAxes': [
              {
                'scaleLabel': {
                  'display': 'true',
                  'labelString': 'Current Published Time'
                },
              },
            ],
            'yAxes': [
              {
                  'scaleLabel': {
                    'display': 'true',
                    'labelString': 'Number of Articles',
                },
              },
            ],
          },
        'plugins': {
          'datalabels': {
            'display': 'true',
            'align': 'top',
            'backgroundColor': '#ccc',
            'color':'black',
            'borderRadius': 3
           },
          }
        }
      }
  chart.to_file('tmp/volume_widget.png')
  chart.to_file('tmp/clipping_feed_content_widget.png')
