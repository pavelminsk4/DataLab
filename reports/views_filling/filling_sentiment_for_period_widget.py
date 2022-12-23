from .options import *

def sentiment_for_period_widget_image(document, proj):
  if proj.sentiment_for_period_widget.is_active:
    p2 = document.add_paragraph(' Sentiment For Period Widget', style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p2.paragraph_format.element.get_or_add_pPr()
    p2.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture('tmp/sentiment_for_period_widget.png', width=Inches(6.6))
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_paragraph('', style='pTableHeaderLeft')
  return True
