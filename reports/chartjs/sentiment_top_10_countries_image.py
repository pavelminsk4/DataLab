from widgets.common_widget.sentiment_top_10_countries_widget import *
from project.models import *
from quickchart import QuickChart

def create_sentiment_top_10_countries_wid_image(project_id):
  proj = Project.objects.get(id=project_id)
  posts = posts_agregator(proj)
  top_countries = posts.values('feedlink__country').annotate(brand_count=Count('feedlink__country')).order_by('-brand_count').values_list('feedlink__country', flat=True)[:10]
  results = {country: list(posts.filter(feedlink__country=country).values('sentiment').annotate(sentiment_count=Count('sentiment')).order_by('-sentiment_count')) for country in top_countries}
  for i in range(len(results)):
    sentiments = ['negative', 'neutral', 'positive']
    for j in range(len(results[top_countries[i]])):
      for sen in sentiments:
        if sen in results[top_countries[i]][j].get('sentiment'):
          sentiments.remove(sen)
    for sen in sentiments:
      results[top_countries[i]].append({'sentiment': sen, 'sentiment_count': 0})
  res = {}
  for key in results:
    if key == '' or key == None or 'img' in key or key == 'None' or key == 'null' or not key:
      res['Missing in source'] = results[key]    
    else:  
      res[key] = results[key]    
  labels_list = [country for country in res]
  data_neutral = []
  data_negative = []
  data_positive = []

  for country in labels_list:
    for i in range(len(res[country])):
      if res[country][i]['sentiment'] == 'neutral':
        data_neutral.append(res[country][i]['sentiment_count'])
      if res[country][i]['sentiment'] == 'negative':
        data_negative.append(res[country][i]['sentiment_count'])
      if res[country][i]['sentiment'] == 'positive':
        data_positive.append(res[country][i]['sentiment_count'])  

  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  qc.config = {
    'type': 'bar',
    'data': {
      'labels': labels_list,
      'datasets': [
        {
          'label': 'negative',
          'data': data_negative,
          'backgroundColor': ['rgba(150,109,49,255)'],
        },
        {
          'label': 'neutral',
          'data': data_neutral,
          'backgroundColor': ['rgba(43,151,88,255)'],
        },
        {
          'label': 'positive',
          'data': data_positive,
          'backgroundColor': ['rgba(125,52,54,255)'],
        },   
      ],   
    },  
    'options': {
      'plugins': {
        'roundedBars': True 
            },
          },
        }
  qc.to_file('tmp/sentiment_top_10_countries_widget.png')
