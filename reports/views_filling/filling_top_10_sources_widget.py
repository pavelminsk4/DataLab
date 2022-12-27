from .options import *

def top_10_sources_widget_image(document, proj):
  if proj.top_10_brands_widget.is_active:
    widget_image(document, ' Top 10 Brands Widget', 'tmp/top_10_sources_widget.png')
  return True
