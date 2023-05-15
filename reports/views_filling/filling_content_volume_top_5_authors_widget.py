from .options import *

def content_volume_top_5_authors_widget_image(document, proj):
  if proj.content_volume_top_authors.is_active:
    widget_image(document, ' Content Volume Top 10 Authors Widget', 'tmp/content_volume_top_5_authors_widget.png')
  return True
