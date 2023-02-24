from widgets.common_widget.volume_widget import *
from project.models import *
from quickchart import QuickChart

def create_vol_widget_image(project_id, widget_pk):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  smpl_freq = proj.widgets_list_2.volume_widget.aggregation_period
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
              'lineTension': 0.6,
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
        }
      }
  }
  chart.to_file('tmp/volume_widget.png')
