from .options import *

def volume_widget_image(document, proj):
  if proj.volume_widget.is_active:
    widget_image(document, ' Volume Widget (per day)', 'tmp/volume_widget.png')
  return True
