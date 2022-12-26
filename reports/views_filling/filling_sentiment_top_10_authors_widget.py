from .options import *

def sentiment_top_10_authors_widget_image(document, proj):
  if proj.sentiment_top_10_authors_widget.is_active:
    widget_image(document, ' Sentiment Top 10 Authors Widget', 'tmp/sentiment_top_10_authors_widget.png') 
  return True
