from .options import *

def sentiment_for_period_widget_image(document, proj):
  if proj.sentiment_for_period_widget.is_active:
    widget_image(document, ' Sentiment For Period Widget', 'tmp/sentiment_for_period_widget.png')
  return True
