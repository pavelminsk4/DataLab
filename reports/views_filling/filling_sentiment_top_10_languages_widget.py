from .options import *

def sentiment_top_10_languages_widget_image(document, proj):
  if proj.sentiment_top_languages.is_active:
    widget_image(document, ' Sentiment Top 10 Languages Widget', 'tmp/sentiment_top_10_languages_widget.png')
  return True
