from .options import *

def content_volume_top_5_source_widget_image(document, proj):
  if proj.content_volume_top_sources.is_active:
    widget_image(document, ' Content Volume Top 5 Source Widget', 'tmp/content_volume_top_5_source_widget.png')
  return True
