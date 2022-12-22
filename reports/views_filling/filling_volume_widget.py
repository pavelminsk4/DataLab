from .options import *

def volume_widget_image(document, proj):
  if proj.volume_widget.is_active:
    p4 = document.add_paragraph(' Volume Widget (per day)', style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p4.paragraph_format.element.get_or_add_pPr()
    p4.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture('tmp/volume_widget.png', width=Inches(6.6))
    document.add_paragraph('', style='pTableHeaderLeft')
  return True
