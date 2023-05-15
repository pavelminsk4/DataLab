from .options import *

def top_10_countries_widget_image(document, proj):
  if proj.top_countries.is_active:
    widget_image(document, ' Top 10 Countries Widget', 'tmp/top_10_countries_widget.png')
  return True
