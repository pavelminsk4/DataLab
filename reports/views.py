from project_social.widgets.dashboard.top_languages import top_languages_report
from project_social.widgets.dashboard.top_authors import top_authors_report
from project_social.widgets.dashboard.top_locations import top_locations_report
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
from django.shortcuts import render
from project_social.models import ProjectSocial, SocialWidgetsList
from reports.classes.social_pdf import SocialPDF
from reports.classes.converter import Converter
from project_social.widgets.dashboard.content_volume_top_languages import content_volume_top_languages_report
from project_social.widgets.dashboard.content_volume_top_locations import content_volume_top_locations_report
from project_social.widgets.dashboard.content_volume_top_authors import content_volume_top_authors_report
from project_social.widgets.sentiment.sentiment_number_of_results import sentiment_report
from project_social.widgets.dashboard.sentiment_authors import sentiment_authors_report
from project_social.widgets.dashboard.content_volume import content_volume_report 


def filling_template(template_path, project_id):
    document = Document(template_path)
    document = filling_templates_for_instant_and_regular_reports(
        document, project_id)
    document.save('tmp/temp.docx')

def report_generator(proj_pk, model):
    template_path = 'static/report_templates/RSDC_Export_Template_EN.docx'
    docx_path = 'tmp/temp.docx'
    report_path = 'tmp/temp.pdf'
    proj = model.objects.get(id=proj_pk)
    if model == Project:
        prepare_widget_images(proj_pk)
        filling_template(template_path, proj_pk)
        convert_docx_to_pdf(docx_path, report_path)
    if model == ProjectSocial:
        item = Converter(proj).convert_to_item()
        report_path = SocialPDF(item, 'pdf', template_path).generate()
    response = FileResponse(open(report_path, 'rb'))
    response.headers = {
        'Content-Type': 'application/%s' % (format),
        'Content-Disposition': 'attachment;filename="report.%s"' % (format),
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


def social_top_locations_screenshot(request,proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_locations.pk
    context = top_locations_report(proj_pk, wd_pk)
    return render(request, 'social_reports/top_locations_screenshot.html', context)


def social_top_authors_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_authors.pk
    context = top_authors_report(proj_pk, wd_pk)
    return render(request, 'social_reports/top_authors_screenshot.html', context)


def social_top_languages_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_languages.pk
    context = top_languages_report(proj_pk, wd_pk)
    return render(request, 'social_reports/top_languages_screenshot.html', context)

def social_sentiment_diagram_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_diagram.pk
    context = {'context': sentiment_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)

def social_content_volume_top_authors_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).content_volume_top_authors.pk
    context = {'context': content_volume_top_authors_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)

def social_content_volume_top_languages_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).content_volume_top_languages.pk
    context = {'context': content_volume_top_languages_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)

def social_content_volume_top_locations_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).content_volume_top_locations.pk
    context = {'context': content_volume_top_locations_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)

def social_content_volume_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).content_volume.pk
    context = {'context': content_volume_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)

def social_sentiment_authors_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_authors.pk
    context = {'context': sentiment_authors_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)
