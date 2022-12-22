from widgets.common_widget.top_10_languages_widget import *
from project.models import *
from quickchart import QuickChart

def create_top_10_languages_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  results = posts.values('feed_language__language').annotate(language_count=Count('feed_language__language')).order_by('-language_count')[:10]
  for i in range(len(results)):
    if (results[i]['feed_language__language'] == None or not results[i]['feed_language__language'] or 'img' in results[i]['feed_language__language'] or results[i]['feed_language__language'] == 'None' or results[i]['feed_language__language'] == 'null' or results[i]['feed_language__language'] == 'Language not specified'):
      results[i]['feed_language__language'] = 'Missing in source'
  labels = []
  data = []
  for each in results:
    labels.append(each['feed_language__language'])
    data.append(each['language_count'])
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
      'legend': {
          'position': 'bottom',
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
  qc.to_file('tmp/top_10_languages_widget.png')
