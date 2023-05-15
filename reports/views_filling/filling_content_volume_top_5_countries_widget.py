from .options import *

def content_volume_top_5_countries_widget_image(document, proj):
  if proj.content_volume_top_countries.is_active:
    widget_image(document, ' Content Volume Top 5 Countries Widget', 'tmp/content_volume_top_5_countries_widget.png')
  return True
