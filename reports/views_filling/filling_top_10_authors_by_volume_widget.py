from .options import *

def top_10_authors_by_volume_widget_image(document, proj):  
  if proj.top_10_authors_by_volume_widget.is_active:
    widget_image(document, ' Top 10 Authors By Volume Widget', 'tmp/top_10_authors_by_volume_widget.png')
  return True
