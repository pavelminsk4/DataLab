from quickchart import QuickChart

def prepare_widget_image(project_id):
  chart = QuickChart()
  chart.width = 900
  chart.height = 450
  chart.config = {
      "type": "pie",
      "data":{
          "labels": ['test', 'lol', 'kek'],
          "datasets": [
            {
              "borderColor": '#055FFC',
              "pointStyle": 'circle',
              "borderWidth": 0,
              "borderRadius": 6,
              "barPercentage": 0.5,
              "fill": True,
              "tension": 0.25,
              "data": [1,2,3],
          
            },
          ],
        },
      "options": {
          "responsive": True,
          "maintainAspectRatio": False,
          "animation": {
            "easing": 'easeInOutQuad',
            "duration": 520,
          },
          "plugins": {
            "legend": {
              "display": False,
            },
            "tooltip": {
              "yAlign": 'bottom',
              "titleColor": '#151515',
              "bodyColor": '#151515',
              "backgroundColor": 'rgba(255, 255, 255, 0.96)',
              "displayColors": False,
            },
          },
          "scales": {
            "y": {
              "beginAtZero": True,
              "grid": {
                "color": 'rgba(145, 152, 167, 0.1)',
              },
            },
            "x": {
              "beginAtZero": True,
              "grid": {
                "display": False,
              },
            },
          },
      },
  }
  chart.to_file('tmp/summary_widget.png')
  chart.to_file('tmp/top_10_authors_by_volume_widget.png')
  chart = QuickChart()
  chart.width = 900
  chart.height = 450
  chart.config = {
      "type": "bar",
      "data":{
          "labels": ['test', 'lol', 'kek'],
          "datasets": [
            {
              "borderColor": '#055FFC',
              "pointStyle": 'circle',
              "borderWidth": 0,
              "borderRadius": 6,
              "barPercentage": 0.5,
              "fill": True,
              "tension": 0.25,
              "data": [1,2,3],
          
            },
          ],
        },
      "options": {
          "responsive": True,
          "maintainAspectRatio": False,
          "animation": {
            "easing": 'easeInOutQuad',
            "duration": 520,
          },
          "plugins": {
            "legend": {
              "display": False,
            },
            "tooltip": {
              "yAlign": 'bottom',
              "titleColor": '#151515',
              "bodyColor": '#151515',
              "backgroundColor": 'rgba(255, 255, 255, 0.96)',
              "displayColors": False,
            },
          },
          "scales": {
            "y": {
              "beginAtZero": True,
              "grid": {
                "color": 'rgba(145, 152, 167, 0.1)',
              },
            },
            "x": {
              "beginAtZero": True,
              "grid": {
                "display": False,
              },
            },
          },
      },
  }
  chart.to_file('tmp/volume_widget.png')
  chart.to_file('tmp/clipping_feed_content_widget.png')
