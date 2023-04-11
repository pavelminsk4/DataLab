from django.http import FileResponse
from project.models import Project
from project_social.models import ProjectSocial
from docx import Document
from .chartjs.chartjs import prepare_widget_images
from .serializers import RegularReportSerializer
from .models import RegularReport
from rest_framework import viewsets
from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports
from .services.pdf_handler import convert_docx_to_pdf

def filling_template(template_path, project_id):
  document = Document(template_path)
  document = filling_templates_for_instant_and_regular_reports(document, project_id)
  document.save('tmp/temp.docx')

def prepare_social_widget_images(proj_pk):
  return True

def filling_social_template(template_path, proj_pk):
  return True

def report_generator(proj_pk, model):
  proj = model.objects.get(id=proj_pk)
  format = proj.report_format
  template_path = str(proj.report_template.layout_file)
  docx_path = 'tmp/temp.docx'
  report_path = 'tmp/temp.' + format
  if model == Project:
    prepare_widget_images(proj_pk)
    filling_template(template_path, proj_pk)
  if model == ProjectSocial:
    prepare_social_widget_images(proj_pk)
    filling_social_template(template_path, proj_pk)
  convert_docx_to_pdf(docx_path, report_path)
  response = FileResponse(open(report_path, 'rb'))
  response.headers = {
      'Content-Type': 'application/%s'%(format),
      'Content-Disposition': 'attachment;filename="report.%s"'%(format),
  }
  response.as_attachment = True
  return response


def online_instantly_report(request, proj_pk, dep_pk):
  return report_generator(proj_pk, Project)

def social_instantly_report(request, proj_pk, dep_pk):
  return report_generator(proj_pk, ProjectSocial)

class RegularReportViewSet(viewsets.ModelViewSet):
  serializer_class = RegularReportSerializer
  def get_queryset(self):
    return RegularReport.objects.filter(department_id=self.kwargs['dep_pk'])
