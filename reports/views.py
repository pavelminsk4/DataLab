from django.http import FileResponse
from .models import Templates
from project.models import Project
from widgets.models import WidgetsList2
from django.shortcuts import get_object_or_404
from docx import Document
from docx.shared import Inches
from .chartjs import prepare_widget_images
import aspose.words as aw

lic = aw.License()

#Try to set license from the folder with the python script.
try :
    lic.set_license("Aspose.Total.Product.Family.lic")
    print("License set successfully.")
except RuntimeError as err :
    # We do not ship any license with this example, visit the Aspose site to obtain either a temporary or permanent license.
    print("\nThere was an error setting the license: {0}".format(err))

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

def convert_docx_to_pdf(docx_path, report_path):
  doc = aw.Document(docx_path)
  doc.save(report_path)

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
              cell.add_paragraph('\u2140' + '   ' + proj.summary_widget.title, style='pTOC1',)
              cell.add_paragraph('Description: ' + proj.summary_widget.aggregation_period, style='pTOC2')
            if proj.top_10_authors_by_volume_widget.is_active:
              cell.add_paragraph('\u21F5' + '   ' + proj.top_10_authors_by_volume_widget.title, style='pTOC1')
              cell.add_paragraph('Description: ' + proj.top_10_authors_by_volume_widget.aggregation_period, style='pTOC2')
            if proj.volume_widget.is_active:
              cell.add_paragraph('\u2023' + '   ' + proj.volume_widget.title, style='pTOC1')
              cell.add_paragraph('Date Aggregation Period: ' + proj.volume_widget.aggregation_period, style='pTOC2')
            if proj.clipping_feed_content_widget.is_active:
              cell.add_paragraph('\u2704' + '   ' + proj.clipping_feed_content_widget.title, style='pTOC1')
              cell.add_paragraph('Description: ' + proj.clipping_feed_content_widget.aggregation_period, style='pTOC2')
  # if proj.summary_widget.is_active:
  #   table = document.add_table(rows=1, cols=1)
  #   hdr_cells = table.rows[0].cells
  #   hdr_cells[0].add_paragraph('Summary Widget', style='pExportTitle')
  #   document.add_picture('tmp/summary_widget.png', width=Inches(6.6))
  #   document.add_page_break()
  if proj.top_10_authors_by_volume_widget.is_active:
    table = document.add_table(rows=1, cols=1)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].add_paragraph('Top 10 Authors By Volume Widget', style='pExportTitle')
    document.add_picture('tmp/top_10_authors_by_volume_widget.png', width=Inches(6.6))
    document.add_page_break()
  if proj.volume_widget.is_active:
    table = document.add_table(rows=1, cols=1)
    hdr_cells = table.rows[0].cells
    hdr_cells[0].add_paragraph('Volume Widget', style='pExportTitle')
    document.add_picture('tmp/volume_widget.png', width=Inches(6.6))
    document.add_page_break()
  # if proj.clipping_feed_content_widget.is_active:
  #   table = document.add_table(rows=1, cols=1)
  #   hdr_cells = table.rows[0].cells
  #   hdr_cells[0].add_paragraph('Clipping Feed Content Widget', style='pExportTitle')
  #   document.add_picture('tmp/clipping_feed_content_widget.png', width=Inches(6.6))
  #   document.add_page_break()
  document.save('tmp/temp.docx')

def instantly_report(request, pk):
  proj = Project.objects.get(id=pk)
  format = proj.report_format
  template_path = str(proj.report_template.layout_file)
  docx_path='tmp/temp.docx'
  report_path='tmp/temp.' + format
  prepare_widget_images(pk)
  filling_template(template_path, pk)
  convert_docx_to_pdf(docx_path, report_path)
  response = FileResponse(open(report_path, 'rb'))
  response.headers = {
      'Content-Type': 'application/%s'%(format),
      'Content-Disposition': 'attachment;filename="report.%s"'%(format),
  }
  response.as_attachment = True
  return response
