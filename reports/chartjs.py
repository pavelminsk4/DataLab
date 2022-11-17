from quickchart import QuickChart
from widgets.common_widget.volume_widget import *
from project.models import *

def create_vol_widget_image(project_id):
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

def create_top_10_authors_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  res = posts.values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:10]
  labels = []
  data = []
  for each in res:
    labels.append(each['entry_author'])
    data.append(each['author_posts_count'])
  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  qc.config ={
    'type': 'doughnut',
    'data': {
      'datasets': [
        {
          'data': data,
          'backgroundColor': [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(14, 162, 235)',
            'rgb(24, 162, 225)',
            'rgb(34, 162, 205)',
            'rgb(44, 162, 191)',
            'rgb(50, 162, 172)',
            'rgb(54, 162, 153)',
          ],
        },
      ],
      'labels': labels,
    },
    'options': {
      'legend': {
          'position': 'bottom',
          },
      'title': {
        'display': 'true',
        'text': proj.title,
        'position': 'bottom',
      },
    },
  }
  qc.to_file('tmp/top_10_authors_by_volume_widget.png')

def prepare_widget_images(project_id):
  create_vol_widget_image(project_id)
  create_top_10_authors_wid_image(project_id)

