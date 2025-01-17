from project_social.widgets.dashboard.content_volume_top_languages import content_volume_top_languages_report
from project_social.widgets.dashboard.content_volume_top_locations import content_volume_top_locations_report
from project_social.widgets.sentiment.sentiment_number_of_results import sentiment_number_of_results_report
from project_social.widgets.dashboard.content_volume_top_authors import content_volume_top_authors_report
from project_social.widgets.sentiment.sentiment_top_keywords import sentiment_top_keywords_report
from project_social.widgets.demography.top_authors_by_gender import top_authors_by_gender_report
from project_social.widgets.demography.languages_by_location import languages_by_location_report
from project_social.widgets.influencers.authors_by_sentiment import authors_by_sentiment_report
from project_social.widgets.demography.keywords_by_location import keywords_by_location_report
from project_social.widgets.influencers.top_sharing_sources import top_sharing_sources_report
from project_social.widgets.demography.authors_by_language import authors_by_language_report
from project_social.widgets.demography.authors_by_location import authors_by_location_report
from project_social.widgets.dashboard.sentiment_languages import sentiment_languages_report
from project_social.widgets.dashboard.sentiment_locations import sentiment_locations_report
from project_social.widgets.sentiment.sentiment_by_gender import sentiment_by_gender_report
from project_social.widgets.demography.gender_by_location import gender_by_location_report
from project_social.widgets.demography.authors_by_gender import authors_by_gender_report
from project_social.widgets.dashboard.sentiment_authors import sentiment_authors_report
from project_social.widgets.dashboard.content_volume import content_volume_report
from project_social.widgets.dashboard.top_languages import top_languages_report
from project_social.widgets.dashboard.top_locations import top_locations_report
from project_social.widgets.summary.gender_volume import gender_volume_report
from project_social.widgets.dashboard.top_authors import top_authors_report
from project_social.widgets.summary.top_keywords import top_keywords_report
from project_social.widgets.dashboard.summary_widget import summary_report
from project_social.widgets.dashboard.sentiment import sentiment_report

from widgets.common_widget.content_volume_top_countries import content_volume_top_countries_report as onl_content_volume_top_countries
from widgets.common_widget.content_volume_top_sources import content_volume_top_sources_report as onl_content_volume_top_sources
from widgets.common_widget.content_volume_top_authors import content_volume_top_authors_report as onl_content_volume_top_authors
from widgets.common_widget.sentiment_top_countries import sentiment_top_countries_report as onl_sentiment_top_countries
from widgets.common_widget.sentiment_top_languages import sentiment_top_languages_report as onl_sentiment_top_languages
from widgets.demography.top_keywords_by_country import get_keywords_by_country_report as onl_top_keywords_by_country
from widgets.common_widget.sentiment_top_sources import sentiment_top_sources_report as onl_sentiment_top_sources
from widgets.common_widget.sentiment_top_authors import sentiment_top_authors_report as onl_sentiment_top_authors
from widgets.sentiment.sentiment_top_keywords import sentiment_top_keywords_report as onl_sentiment_top_keywords
from widgets.influencers.authors_by_sentiment import get_authors_by_sentiment_report as onl_authors_by_sentiment
from widgets.demography.languages_by_country import get_languages_by_country_report as onl_languages_by_country
from widgets.demography.sources_by_language import get_sources_by_language_report as onl_sources_by_language
from widgets.influencers.authors_by_language import get_authors_by_language_report as onl_authors_by_language
from widgets.influencers.overall_top_authors import get_overall_top_authors_report as onl_overall_top_authors
from widgets.demography.top_sharing_sources import get_top_sharing_sources_report as onl_top_sharing_sources
from widgets.demography.overall_top_sources import get_overall_top_sources_report as onl_overall_top_sources
from widgets.sentiment.sentiment_number_of_results import number_of_results_report as onl_number_of_results
from widgets.sentiment.sentiment_number_of_results import sentiment_diagram_report as onl_sentiment_diagram
from widgets.common_widget.sentiment_for_period import sentiment_for_period_report as onl_sentiment_report
from widgets.influencers.authors_by_country import get_authors_by_country_report as onl_authors_by_country
from widgets.demography.sources_by_country import get_sources_by_country_report as onl_sources_by_country
from widgets.common_widget.top_sources import top_sources_report as onl_top_sources_report
from widgets.common_widget.top_authors import top_authors_report as onl_top_authors_report
from widgets.common_widget.top_languages import top_languages_report as onl_top_languages
from widgets.common_widget.top_countries import top_countries_report as onl_top_countries

from widgets.summary.top_keywords import top_keywords_report as onl_top_keywords_report
from widgets.common_widget.volume_widget import volume_report as onl_volume_report
from widgets.common_widget.summary import summary_report as onl_summary_report

from reports.views_filling.filling_for_report import filling_templates_for_instant_and_regular_reports
from .serializers import RegularReportSerializer
from django.http import FileResponse
from rest_framework import viewsets
from django.shortcuts import render
from .models import RegularReport
from docx import Document

from project_social.models import ProjectSocial, SocialWidgetsList
from widgets.models import WidgetsList2
from project.models import Project

from reports.classes.social_pdf import SocialPDF
from reports.classes.online_pdf import OnlinePDF
from reports.classes.converter import Converter


def filling_template(template_path, project_id):
    document = Document(template_path)
    document = filling_templates_for_instant_and_regular_reports(
        document, project_id)
    document.save('tmp/temp.docx')


def report_generator(proj_pk, model):
    template_path = 'fixtures/report_templates/RSDC_Export_Template_EN.docx'
    report_path = 'tmp/temp.pdf'
    proj = model.objects.get(id=proj_pk)
    if model == Project:
        item = Converter(proj).convert_to_item()
        report_path = OnlinePDF(item, 'pdf', template_path).generate()
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


def online_instantly_report(request, proj_pk):
    return report_generator(proj_pk, Project)


def social_instantly_report(request, proj_pk):
    return report_generator(proj_pk, ProjectSocial)


class RegularReportViewSet(viewsets.ModelViewSet):
    serializer_class = RegularReportSerializer

    def get_queryset(self):
        return RegularReport.objects.filter(department_id=self.request.user.user_profile.department_id)


def social_top_locations_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_locations.pk
    context = {'context': top_locations_report(proj_pk, wd_pk, 'top_locations')}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_top_authors_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_authors.pk
    context = {'context': top_authors_report(proj_pk, wd_pk, 'top_authors')}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_top_languages_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_languages.pk
    context = {'context': top_languages_report(proj_pk, wd_pk, 'top_languages')}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_diagram_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_diagram.pk
    context = {'context': sentiment_number_of_results_report(proj_pk, wd_pk, 'sentiment_diagram')}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_number_of_results_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_number_of_results.pk
    context = {'context': sentiment_number_of_results_report(proj_pk, wd_pk, 'sentiment_number_of_results')}
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


def social_sentiment_languages_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_languages.pk
    context = {'context': sentiment_languages_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_locations_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_locations.pk
    context = {'context': sentiment_locations_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_summary_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).summary.pk
    context = {'context': summary_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_gender_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_by_gender.pk
    context = {'context': sentiment_by_gender_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment.pk
    context = {'context': sentiment_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_top_keywords_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_keywords.pk
    context = {'context': top_keywords_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_top_authors_by_gender_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_authors_by_gender.pk
    context = {'context': top_authors_by_gender_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_authors_by_gender_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).authors_by_gender.pk
    context = {'context': authors_by_gender_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_authors_by_language_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).authors_by_language.pk
    context = {'context': authors_by_language_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_authors_by_location_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).authors_by_location.pk
    context = {'context': authors_by_location_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_gender_by_location_screenshot_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).gender_by_location.pk
    context = {'context': gender_by_location_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_keywords_by_location_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).keywords_by_location.pk
    context = {'context': keywords_by_location_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_languages_by_location_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).languages_by_location.pk
    context = {'context': languages_by_location_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_top_sharing_sources_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).top_sharing_sources.pk
    context = {'context': top_sharing_sources_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_gender_volume_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).gender_volume.pk
    context = {'context': gender_volume_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_sentiment_top_keywords_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).sentiment_top_keywords.pk
    context = {'context': sentiment_top_keywords_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def social_authors_by_sentiment_screenshot(request, proj_pk):
    wd_pk = SocialWidgetsList.objects.get(project_id=proj_pk).authors_by_sentiment.pk
    context = {'context': authors_by_sentiment_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_summary_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).summary.pk
    context = {'context': onl_summary_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_volume_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).volume.pk
    context = {'context': onl_volume_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_for_period.pk
    context = {'context': onl_sentiment_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_sources_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_sources.pk
    context = {'context': onl_top_sources_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_authors_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_authors.pk
    context = {'context': onl_top_authors_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_keywords_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_keywords.pk
    context = {'context': onl_top_keywords_report(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_number_of_results_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_number_of_results.pk
    context = {'context': onl_number_of_results(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_diagram_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_diagram.pk
    context = {'context': onl_sentiment_diagram(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_top_sources_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_top_sources.pk
    context = {'context': onl_sentiment_top_sources(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_top_authors_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_top_authors.pk
    context = {'context': onl_sentiment_top_authors(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_top_countries_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_top_countries.pk
    context = {'context': onl_sentiment_top_countries(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_top_languages_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_top_languages.pk
    context = {'context': onl_sentiment_top_languages(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sentiment_top_keywords_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sentiment_top_keywords.pk
    context = {'context': onl_sentiment_top_keywords(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sources_by_country_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sources_by_country.pk
    context = {'context': onl_sources_by_country(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_authors_by_country_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).authors_by_country.pk
    context = {'context': onl_authors_by_country(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_languages_by_country_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).languages_by_country.pk
    context = {'context': onl_languages_by_country(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_keywords_by_country_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_keywords_by_country.pk
    context = {'context': onl_top_keywords_by_country(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_sharing_sources_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_sharing_sources.pk
    context = {'context': onl_top_sharing_sources(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_authors_by_language_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).authors_by_language.pk
    context = {'context': onl_authors_by_language(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_overall_top_sources_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).overall_top_sources.pk
    context = {'context': onl_overall_top_sources(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_overall_top_authors_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).overall_top_authors.pk
    context = {'context': onl_overall_top_authors(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_authors_by_sentiment_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).authors_by_sentiment.pk
    context = {'context': onl_authors_by_sentiment(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_sources_by_language_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).sources_by_language.pk
    context = {'context': onl_sources_by_language(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_countries_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_countries.pk
    context = {'context': onl_top_countries(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_top_languages_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).top_languages.pk
    context = {'context': onl_top_languages(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_content_volume_top_sources_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).content_volume_top_sources.pk
    context = {'context': onl_content_volume_top_sources(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_content_volume_top_authors_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).content_volume_top_authors.pk
    context = {'context': onl_content_volume_top_authors(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)


def online_content_volume_top_countries_screenshot(request, proj_pk):
    wd_pk = WidgetsList2.objects.get(project_id=proj_pk).content_volume_top_countries.pk
    context = {'context': onl_content_volume_top_countries(proj_pk, wd_pk)}
    return render(request, 'social_reports/base_template_screenshot.html', context)
