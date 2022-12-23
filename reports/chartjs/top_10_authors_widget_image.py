from widgets.common_widget.top_10_authors_by_volume_widget import *
from project.models import *
from quickchart import QuickChart

def create_top_10_authors_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  results = posts.values('entry_author').annotate(author_posts_count=Count('entry_author')).order_by('-author_posts_count')[:10]
  for i in range(len(results)):
    if (results[i]['entry_author'] == None or not results[i]['entry_author'] or 'img' in results[i]['entry_author'] or results[i]['entry_author'] == 'None' or results[i]['entry_author'] == 'null'):
      results[i]['entry_author'] = 'Missing in source'  
  labels = []
  data = []
  for each in results:
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
  qc.to_file('tmp/top_10_authors_by_volume_widget.png')
