from django.http import FileResponse
from .models import Templates
from widgets.models import ClippingFeedContentWidget
from project.models import Project
from widgets.models import WidgetsList2
from django.shortcuts import get_object_or_404
from docx import Document
from docx.shared import Inches, Pt
from .chartjs.chartjs import prepare_widget_images
import aspose.words as aw
from .serializers import RegularReportSerializer
from .models import RegularReport
from rest_framework import viewsets
from reports.views_filling.filling_summary_widget import summarry_widget_image
from reports.views_filling.filling_volume_widget import volume_widget_image
from reports.views_filling.filling_top_10_authors_by_volume_widget import top_10_authors_by_volume_widget_image
from reports.views_filling.filling_top_10_sources_widget import top_10_sources_widget_image
from reports.views_filling.filling_top_10_countries_widget import top_10_countries_widget_image
from reports.views_filling.filling_top_10_languages_widget import top_10_languages_widget_image
from reports.views_filling.filling_sentiment_top_10_sources_widget import sentiment_top_10_sources_widget_image
from reports.views_filling.filling_sentiment_top_10_authors_widget import sentiment_top_10_authors_widget_image
from reports.views_filling.filling_sentiment_top_10_countries_widget import sentiment_top_10_countries_widget_image
from reports.views_filling.filling_sentiment_top_10_languages_widget import sentiment_top_10_languages_widget_image
from reports.views_filling.filling_sentiment_for_period_widget import sentiment_for_period_widget_image
from reports.views_filling.filling_content_volume_top_10_source_widget import content_volume_top_10_source_widget_image
from reports.views_filling.filling_content_volume_top_10_authors_widget import content_volume_top_10_authors_widget_image
from reports.views_filling.filling_content_volume_top_10_countries_widget import content_volume_top_10_countries_widget_image
from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports

lic = aw.License()

#Try to set license from the folder with the python script.
try :
    lic.set_license("Aspose.Total.Product.Family.lic")
    print("License set successfully.")
except RuntimeError as err :
    # We do not ship any license with this example, visit the Aspose site to obtain either a temporary or permanent license.
    print("\nThere was an error setting the license: {0}".format(err))

def convert_docx_to_pdf(docx_path, report_path):
  doc = aw.Document(docx_path)
  doc.save(report_path)

def filling_template(template_path, project_id):
  document = Document(template_path)
  document = filling_templates_for_instant_and_regular_reports(document, project_id)
  document.save('tmp/temp.docx')

def instantly_report(request, proj_pk):
  proj = Project.objects.get(id=proj_pk)
  format = proj.report_format
  template_path = str(proj.report_template.layout_file)
  docx_path='tmp/temp.docx'
  report_path='tmp/temp.' + format
  prepare_widget_images(proj_pk)
  filling_template(template_path, proj_pk)
  convert_docx_to_pdf(docx_path, report_path)
  response = FileResponse(open(report_path, 'rb'))
  response.headers = {
      'Content-Type': 'application/%s'%(format),
      'Content-Disposition': 'attachment;filename="report.%s"'%(format),
  }
  response.as_attachment = True
  return response

class RegularReportViewSet(viewsets.ModelViewSet):
  serializer_class = RegularReportSerializer
  def get_queryset(self):
   return RegularReport.objects.filter(project_id=self.kwargs['proj_pk'])
