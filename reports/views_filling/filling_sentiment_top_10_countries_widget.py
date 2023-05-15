from .options import *

def sentiment_top_10_countries_widget_image(document, proj):
  if proj.sentiment_top_countries.is_active:
    widget_image(document, ' Sentiment Top 10 Countries Widget', 'tmp/sentiment_top_10_countries_widget.png')  
  return True
