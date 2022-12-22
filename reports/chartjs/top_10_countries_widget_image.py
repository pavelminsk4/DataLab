from widgets.common_widget.top_10_countries_widget import *
from project.models import *
from quickchart import QuickChart

def create_top_10_countries_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  results = posts.values('feedlink__country').annotate(country_count=Count('feedlink__country')).order_by('-country_count')[:10]
  for i in range(len(results)):
    if (results[i]['feedlink__country'] == None or not results[i]['feedlink__country'] or 'img' in results[i]['feedlink__country'] or results[i]['feedlink__country'] == 'None' or results[i]['feedlink__country'] == 'null'):
      results[i]['feedlink__country'] = 'Missing in source'
  labels = []
  data = []
  for each in results:
    labels.append(each['feedlink__country'])
    data.append(each['country_count'])
  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  qc.config ={
    'type': 'horizontalBar',
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
      'scales': {
            'xAxes': [
              {
                'scaleLabel': {
                  'display': 'true',
                  'labelString': 'Count of posts'
                },
              },
            ],
          },
      'plugins': {
        'roundedBars': True 
          },
     },
  }
  qc.to_file('tmp/top_10_countries_widget.png')
