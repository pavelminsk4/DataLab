from .options import *

def sentiment_top_10_sources_widget_image(document, proj):
  if proj.sentiment_top_sources.is_active:
    widget_image(document, ' Sentiment Top 10 Sources Widget', 'tmp/sentiment_top_10_sources_widget.png')
  return True
