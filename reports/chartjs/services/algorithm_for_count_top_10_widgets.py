from quickchart import QuickChart

def algorithm_for_count_top_10_widgets(proj, results, field_name, post_counts):
  for i in range(len(results)):
    if (not results[i][field_name] or 'img' in results[i][field_name] or results[i][field_name] == 'None' or results[i][field_name] == 'null'):
      results[i][field_name] = 'Missing in source'
  labels = []
  data = []
  for each in results:
    labels.append(each[field_name])
    data.append(each[post_counts])
  colors = [
            'rgba(72,139,255,255)',
            'rgba(165,197,255,255)',
            'rgba(81,241,145,255)',
            'rgba(164,234,191,255)',
            'rgba(156,96,255,255)',
            'rgba(246,170,55,255)',
            'rgba(253,228,190,255)',
            'rgba(204,173,255,255)',
            'rgba(255,49,49,255)',
            'rgba(252,148,148,255)',
          ],
  qc = QuickChart()
  qc.width = 900
  qc.height = 450
  qc.config ={
        'type': 'doughnut',
        'data': {
        'datasets': [
            {
            'data': data,
            'backgroundColor': colors,
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
            'color': 'black',
            'font': {
            'weight': 'normal',
            },
            },
        },
        },
    }
  return qc
