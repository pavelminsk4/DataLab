from .options import *

def top_10_authors_by_volume_widget_image(document, proj):  
  if proj.top_10_authors_by_volume_widget.is_active:
    p2 = document.add_paragraph(' Top 10 Authors By Volume Widgett', style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p2.paragraph_format.element.get_or_add_pPr()
    p2.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture('tmp/top_10_authors_by_volume_widget.png', width=Inches(6.6))
    document.add_paragraph('', style='pTableHeaderLeft')
  return True