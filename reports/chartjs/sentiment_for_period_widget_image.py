from widgets.common_widget.sentiment_for_period_widget import *
from project.models import *
from quickchart import QuickChart

def create_sentiment_for_period_widget_image(project_id, widget_pk):
  proj = Project.objects.get(id=project_id)
  posts = post_agregator_with_dimensions(proj)
  widget = WidgetDescription.objects.get(id=widget_pk)
  posts = post_agregetor_for_each_widget(widget, posts)
  smpl_freq = proj.widgets_list_2.sentiment_for_period_widget.aggregation_period
  negative_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='negative').annotate(count_negative=Count('sentiment')).order_by("date")
  neutral_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='neutral').annotate(count_neutral=Count('sentiment')).order_by("date")
  positive_posts = posts.annotate(date=Trunc('entry_published', smpl_freq)).values("date").filter(sentiment='positive').annotate(count_positive=Count('sentiment')).order_by("date")
  post_by_sentiment = list(negative_posts) + list(neutral_posts) + list(positive_posts)
  results = []
  for date in sorted(list(set(d['date'] for d in post_by_sentiment))):
    negative, neutral, positive = 0, 0, 0
    for count_post in post_by_sentiment:
      if date == count_post['date']:
        negative += (count_post.get("count_negative") if count_post.get("count_negative") else 0)
        neutral += (count_post.get("count_neutral") if count_post.get("count_neutral") else 0)
        positive += (count_post.get("count_positive") if count_post.get("count_positive") else 0)
    results.append({str(date): {"negative": negative, "neutral": neutral, "positive": positive}})
  
  labels_list = [list(key for key in results[i])[0][:10] for i in range(len(results))]
  data_neutral = []
  data_negative = []
  data_positive = []

  for i in range(len(labels_list)):
    for date in results[i]:
      data_neutral.append(results[i][date]['neutral'])
      data_negative.append(results[i][date]['negative'])
      data_positive.append(results[i][date]['positive'])  

  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  qc.config = {
    'type': 'bar',
    'data': {
      'labels': labels_list,
      'datasets': [
        {
          'label': 'neutral',
          'data': data_neutral,
          'backgroundColor': ['rgba(246,170,55,255)'],
        },
        {
          'label': 'negative',
          'data': data_negative,
          'backgroundColor': ['rgba(249,71,71,255)'],
        },
        {
          'label': 'positive',
          'data': data_positive,
          'backgroundColor': ['rgba(48,244,126,255)'],
        },   
      ],   
    },  
    'options': {
      'scales': {
        'xAxes': [{
         'ticks': {
            'minRotation': 90
             }
          }]
        },  
      'plugins': {
        'roundedBars': True 
            },
          },
        }
  qc.to_file('tmp/sentiment_for_period_widget.png')
