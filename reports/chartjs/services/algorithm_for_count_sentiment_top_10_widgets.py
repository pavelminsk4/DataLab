from quickchart import QuickChart

def algorithm_for_count_sentiment_top_10_widgets(results, top_list):
  for i in range(len(results)):
    sentiments = ['negative', 'neutral', 'positive']
    for j in range(len(results[top_list[i]])):
      for sen in sentiments:
        if sen in results[top_list[i]][j].get('sentiment'):
          sentiments.remove(sen)
      for sen in sentiments:
        results[top_list[i]].append({'sentiment': sen, 'sentiment_count': 0})
    res = {}
  for key in results:
    if key == '' or key == None or 'img' in key or key == 'None' or key == 'null' or not key or key == 'Language not specified':
      res['Missing in source'] = results[key]    
    else:  
      res[key] = results[key]   
  labels_list = [author for author in res]
  data_neutral = []
  data_negative = []
  data_positive = []
  for author in labels_list:
    for i in range(len(res[author])):
      if res[author][i]['sentiment'] == 'neutral':
        data_neutral.append(res[author][i]['sentiment_count'])
      if res[author][i]['sentiment'] == 'negative':
        data_negative.append(res[author][i]['sentiment_count'])
      if res[author][i]['sentiment'] == 'positive':
        data_positive.append(res[author][i]['sentiment_count'])  
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
  return qc
          