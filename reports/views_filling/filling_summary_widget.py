from .options import *

def summarry_widget_image(document, proj):  
  if proj.summary_widget.is_active:
    p = document.add_paragraph('', style='pExportCoverPageValue')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p.paragraph_format.element.get_or_add_pPr()
    p.paragraph_format.element.pPr.append(shd)
    p = p.add_run(' Report Summary')
    p.font.size = Pt(18)
    document.add_paragraph('', style='pTableHeaderLeft')
    widget_image(document, ' Summary Widget', 'tmp/summary_widget.png')
  return True
