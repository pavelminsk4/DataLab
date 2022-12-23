from celery import shared_task
from email.message import EmailMessage
import smtplib
from reports.models import *

import os
import environ
from pathlib import Path
import mimetypes
import aspose.words as aw

from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml.shared import OxmlElement

from docx import Document
from docx.shared import Inches, Pt
from widgets.models import *

from django.shortcuts import get_object_or_404

BASE_DIR = Path(__file__).resolve().parent.parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))

from .chartjs import prepare_widget_images

# ====================================================================

def export_title(project_id):
  proj = get_object_or_404(Project, pk=project_id)
  title = proj.title
  return title

def export_period(project_id):
  proj = get_object_or_404(Project, pk=project_id)
  start_d = str(proj.start_search_date.ctime())
  end_d = str(proj.end_search_date.ctime())
  period = start_d + ' - ' + end_d
  return period

def filling_template(template_path, project_id):
  document = Document(template_path)
  tbls = document.tables
  for t in tbls:
    for row in t.rows:
      for cell in row.cells:
        for p in cell.paragraphs:
          if '$EXPORT_TITLE$' in p.text:
            p.text = p.text.replace('$EXPORT_TITLE$', export_title(project_id))
          if '$EXPORT_PERIOD$' in p.text:
            p.text = p.text.replace('$EXPORT_PERIOD$', export_period(project_id))
          if '$EXPORT_TOC$' in p.text:
            proj = WidgetsList2.objects.get(project_id=project_id)
            p.text = p.text.replace('$EXPORT_TOC$',' ')
            if proj.summary_widget.is_active:
              cell.add_paragraph('Σ     Report Summary', style='pTOC1',)
              cell.add_paragraph('Summary', style='pTOC2')
            if proj.top_10_authors_by_volume_widget.is_active:
              cell.add_paragraph('↕' + '     ' + proj.top_10_authors_by_volume_widget.title, style='pTOC1')
              cell.add_paragraph('↕ Description: ' + proj.top_10_authors_by_volume_widget.aggregation_period, style='pTOC2')
            if proj.volume_widget.is_active:
              cell.add_paragraph('►' + '    ' + proj.volume_widget.title, style='pTOC1')
              cell.add_paragraph('Date Aggregation Period: ' + proj.volume_widget.aggregation_period, style='pTOC2')
            if proj.clipping_feed_content_widget.is_active:
              cell.add_paragraph('±' + '     ' + proj.clipping_feed_content_widget.title, style='pTOC1')
              cell.add_paragraph('Description: ' + proj.clipping_feed_content_widget.aggregation_period, style='pTOC2')   
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

    p = document.add_paragraph(' Summary Widget', style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p.paragraph_format.element.get_or_add_pPr()
    p.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture('tmp/summary_widget.png', width=Inches(7))
    document.add_page_break()
  if proj.volume_widget.is_active:
    p3 = document.add_paragraph('', style='pExportCoverPageValue')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p3.paragraph_format.element.get_or_add_pPr()
    p3.paragraph_format.element.pPr.append(shd)
    p3 = p3.add_run(' Volume and Potential Reach')
    p3.font.size = Pt(18)
    document.add_paragraph('', style='pTableHeaderLeft')
    
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
  if proj.top_10_authors_by_volume_widget.is_active:
    p1 = document.add_paragraph('', style='pExportCoverPageValue')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p1.paragraph_format.element.get_or_add_pPr()
    p1.paragraph_format.element.pPr.append(shd)
    p1 = p1.add_run(' Volume and Potential Reach')
    p1.font.size = Pt(18)
    document.add_paragraph('', style='pTableHeaderLeft')

    p2 = document.add_paragraph(' Top 10 Authors By Volume Widgett', style='pTableHeaderLeft')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p2.paragraph_format.element.get_or_add_pPr()
    p2.paragraph_format.element.pPr.append(shd)
    document.add_paragraph('', style='pTableHeaderLeft')
    document.add_picture('tmp/top_10_authors_by_volume_widget.png', width=Inches(6.6))
    document.add_page_break()
  #if proj.top_10_brands_widget:

  if proj.clipping_feed_content_widget.is_active:
    p1 = document.add_paragraph('', style='pExportCoverPageValue')
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), '575756')
    p1.paragraph_format.element.get_or_add_pPr()
    p1.paragraph_format.element.pPr.append(shd)
    p1 = p1.add_run(' Clippings: Sample Articles')
    p1.font.size = Pt(18)
    document.add_paragraph('', style='pTableHeaderLeft')

    posts = ClippingFeedContentWidget.objects.filter(project_id=project_id).values(
      'post__entry_title',
      'post__entry_summary',
      'post__entry_published',
      'post__entry_author',
      'post__feedlink__country',
      'post__sentiment',
      )
    for each in posts:
      p = document.add_paragraph(each['post__entry_title'], style='pTableHeaderLeft')
      shd = OxmlElement('w:shd')
      shd.set(qn('w:val'), 'clear')
      shd.set(qn('w:color'), 'auto')
      shd.set(qn('w:fill'), '575756')
      p.paragraph_format.element.get_or_add_pPr()
      p.paragraph_format.element.pPr.append(shd)
      document.add_paragraph(each['post__entry_summary'], style='pPostContent')
      table = document.add_table(rows=2, cols=4)
      for row in table.rows:
        for cell in row.cells:
          shade_obj = OxmlElement('w:shd')
          shade_obj.set(qn('w:fill'), "#ebebeb")
          cell._tc.get_or_add_tcPr().append(shade_obj)# set silver background color
  
      heading_cells = table.rows[0].cells
      heading_cells[0].add_paragraph('Published:', style='pPropertyLabel')
      heading_cells[1].add_paragraph('Author:', style='pPropertyLabel')
      heading_cells[2].add_paragraph('Country:', style='pPropertyLabel')
      heading_cells[3].add_paragraph('Sentiment:', style='pPropertyLabel')
      sec_row = table.rows[1].cells
      sec_row[0].add_paragraph(each['post__entry_published'].strftime("%c"), style='pPropertyValue')
      sec_row[1].add_paragraph(each['post__entry_author'], style='pPropertyValue')
      sec_row[2].add_paragraph(each['post__feedlink__country'], style='pPropertyValue')
      sec_row[3].add_paragraph(each['post__sentiment'], style='pPropertyValue')
      document.add_paragraph('', style='pTableHeaderLeft')
  document.save('tmp/temp_reg_report.docx')


def convert_docx_to_pdf(docx_path, report_path):
  doc = aw.Document(docx_path)
  doc.save(report_path)

def create_pdf_file(reg_report):
  template_path = str(reg_report.template.layout_file)
  docx_path='tmp/temp_reg_report.docx'
  report_path='tmp/temp_reg_report.' + 'pdf'
  prepare_widget_images(reg_report.project.id)
  filling_template(template_path, reg_report.project.pk)
  convert_docx_to_pdf(docx_path, report_path)

# =====================================================================

def send_email_with(file, recipient_list):
  msg = EmailMessage()
  msg['Subject'] = 'Subject: Regular Report from your Anova project.'
  msg['From'] = 'Datalab'
  msg['To'] = recipient_list
  mime_type, _ = mimetypes.guess_type(file)
  mime_type, mime_subtype = mime_type.split('/', 1)
  with open(file, 'rb') as ap:
    msg.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename='report-regular')
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(env('EMAIL_HOST_USER'), env('EMAIL_HOST_PASSWORD'))
    smtp.send_message(msg)

@shared_task
def regular_report_sender(report_id):
  reg_report = RegularReport.objects.get(id=report_id)
  users = reg_report.user.all()
  recipient_list = list(users.values_list('email', flat=True))
  create_pdf_file(reg_report)
  file = './tmp/temp_reg_report.pdf'
  send_email_with(file, recipient_list)