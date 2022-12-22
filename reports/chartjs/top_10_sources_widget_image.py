from widgets.common_widget.top_10_brands_widget import *
from project.models import *
from quickchart import QuickChart

def create_top_10_sources_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  results = posts.values('feedlink__source1').annotate(brand_count=Count('feedlink__source1')).order_by('-brand_count')[:10]
  for i in range(len(results)):
    if (not results[i]['feedlink__source1'] or 'img' in results[i]['feedlink__source1'] or results[i]['feedlink__source1'] == 'None' or results[i]['feedlink__source1'] == 'null'):
      results[i]['feedlink__source1'] = 'Missing in source'
  labels = []
  data = []
  for each in results:
    labels.append(each['feedlink__source1'])
    data.append(each['brand_count'])
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
            'rgba(5,95,252,255)',
            'rgba(122,158,249,255)',
            'rgba(71,249,185,255)',
            'rgba(71,249,121,255)',
            'rgba(149,249,71,255)',
            'rgba(245,249,71,255)',
            'rgba(246,170,55,255)',
            'rgba(246,55,55,255)',
            'rgba(246,55,135,255)',
            'rgba(217,48,244,255)',
          ],
        },
      ],
      'labels': labels,
    },
    'options': {
      'cutoutPercentage': 70,
      'legend': {
          'position': 'right',
          },
      'title': {
        'display': 'true',
        'text': proj.title,
        'position': 'bottom',
      },
    },
    'options': {
      'cutoutPercentage': 70,
      'legend': {
          'position': 'right',
          },
      'title': {
        'display': 'true',
        'text': proj.title,
        'position': 'bottom',
      },
    'plugins': {
      'datalabels': {
        'anchor': 'center',
        'align': 'center',
        'color': 'white',
        'font': {
          'weight': 'normal',
          },  
        },
      },
    },
  }
  qc.to_file('tmp/top_10_sources_widget.png')
