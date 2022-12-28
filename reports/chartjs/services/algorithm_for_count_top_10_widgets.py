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
            'color': 'white',
            'font': {
            'weight': 'normal',
            },
            },
        },
        },
    }
  return qc
