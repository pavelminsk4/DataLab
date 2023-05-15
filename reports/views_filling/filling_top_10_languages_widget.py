from .options import *

def top_10_languages_widget_image(document, proj):
  if proj.top_languages.is_active:
    widget_image(document, ' Top 10 Languages Widget', 'tmp/top_10_languages_widget.png')
  return True
