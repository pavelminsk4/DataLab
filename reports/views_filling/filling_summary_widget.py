from .options import *

def summarry_widget_image(document, proj):  
  if proj.summary_widget.is_active:
    widget_image(document, 'Summary', 'tmp/summary_widget.png')
  return True
