from project_social.models import SocialWidgetDescription, ProjectSocial
from widgets.models import WidgetDescription
from project.models import Project
from django.http import HttpResponse
import csv

import widgets.common_widget.content_volume_top_countries as volume_countries
import widgets.common_widget.sentiment_top_languages as sentiment_languages
import widgets.common_widget.sentiment_top_countries as sentiment_country
import widgets.common_widget.content_volume_top_sources as volume_sources
import widgets.common_widget.content_volume_top_authors as volume_authors
import widgets.sentiment.sentiment_number_of_results as sentiment_number
import widgets.common_widget.sentiment_top_sources as sentiment_sources
import widgets.common_widget.sentiment_top_authors as sentiment_authors
import widgets.demography.top_keywords_by_country as keywords_countries
import widgets.sentiment.sentiment_top_keywords as sentiment_keywords
import widgets.influencers.authors_by_sentiment as authors_sentiment
import widgets.demography.languages_by_country as languages_country
import widgets.influencers.authors_by_language as authors_language
import widgets.demography.sources_by_language as sources_language
import widgets.influencers.authors_by_country as authors_country
import widgets.demography.sources_by_country as sources_country
import widgets.common_widget.sentiment_for_period as sentiment
import widgets.common_widget.top_countries as countries
import widgets.common_widget.top_languages as languages
import widgets.common_widget.volume_widget as volume
import widgets.common_widget.top_authors as authors
import widgets.common_widget.top_sources as sources
import widgets.summary.top_keywords as keywords
import widgets.common_widget.summary as summary

import project_social.widgets.dashboard.content_volume_top_locations as soc_volume_location
import project_social.widgets.dashboard.content_volume_top_languages as soc_volume_language
import project_social.widgets.sentiment.sentiment_number_of_results as soc_sentiment_number
import project_social.widgets.sentiment.sentiment_top_keywords as soc_sentiment_keywords
import project_social.widgets.demography.languages_by_location as soc_languages_location
import project_social.widgets.dashboard.content_volume_top_authors as soc_volume_author
import project_social.widgets.dashboard.sentiment_languages as soc_sentiment_languages
import project_social.widgets.dashboard.sentiment_locations as soc_sentiment_locations
import project_social.widgets.influencers.authors_by_sentiment as soc_author_sentiment
import project_social.widgets.demography.keywords_by_location as soc_keywords_location
import project_social.widgets.sentiment.sentiment_by_gender as soc_sentiment_gender
import project_social.widgets.demography.authors_by_language as soc_author_language
import project_social.widgets.demography.authors_by_location as soc_author_location
import project_social.widgets.dashboard.sentiment_authors as soc_sentiment_authors
import project_social.widgets.demography.gender_by_location as soc_gender_location
import project_social.widgets.demography.authors_by_gender as soc_author_gender
import project_social.widgets.dashboard.top_locations as soc_top_locations
import project_social.widgets.dashboard.top_languages as soc_top_languages
import project_social.widgets.summary.gender_volume as soc_gender_volume
import project_social.widgets.summary.top_keywords as soc_top_keywords
import project_social.widgets.dashboard.top_authors as soc_top_authors
import project_social.widgets.dashboard.summary_widget as soc_summary
import project_social.widgets.dashboard.content_volume as soc_volume
import project_social.widgets.dashboard.sentiment as soc_sentiment


class FactoryCSV:
    def __init__(self, request, module_type, project_pk, widget_pk):
        self.request = request
        self.project_pk = project_pk
        self.widget_pk = widget_pk
        self.module_type = module_type

    def define(self):
        return CSV(self.request, self.project_pk, self.widget_pk).execute(self.module_type)


class CSV:
    def __init__(self, request, project_pk, widget_pk):
        self.request = request
        self.project_pk = project_pk
        self.widget_pk = widget_pk

    def execute(self, module):
        if module == 'online':
            title = WidgetDescription.objects.get(id=self.widget_pk).default_title
        elif module == 'social':
            title = SocialWidgetDescription.objects.get(id=self.widget_pk).default_title
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{title}.csv"'
        writer = csv.writer(response)
        fields, rows = widgets[title].to_csv(self.request, self.project_pk, self.widget_pk)
        writer.writerow(fields)
        for elem in rows:
            writer.writerow(elem)
        return response

widgets = {
    'Summary': summary,
    'Content volume': volume,
    'Top authors': authors,
    'Top sources': sources,
    'Top countries': countries,
    'Top languages': languages,
    'Sentiment for period': sentiment,
    'Content Volume by top sources': volume_sources,
    'Sentiment top sources': sentiment_sources,
    'Sentiment top countries': sentiment_country,
    'Sentiment top authors': sentiment_authors,
    'Sentiment top languages': sentiment_languages,
    'Content volume by top authors': volume_authors,
    'Content volume by top countries': volume_countries,
    'Top keywords': keywords,
    'Sentiment top keywords': sentiment_keywords,
    'Sentiment number of results': sentiment_number,
    'Sentiment diagram': sentiment_number,
    'Authors by country': authors_country,
    'Sources by country': sources_country,
    'Sources by language': sources_language,
    'Authors by language': authors_language,
    'Authors by sentiment': authors_sentiment,
    'Top keywords by country': keywords_countries,
    'Top languages by country': languages_country,
}

social_widgets = {
    'Summary': soc_summary,
    'Top locations': soc_top_locations,
    'Top authors': soc_top_authors,
    'Top languages': soc_top_languages,
    'Content volume': soc_volume,
    'Content volume by top locations': soc_volume_location,
    'Content volume by top authors': soc_volume_author,
    'Content volume by top languages': soc_volume_language,
    'Sentiment': soc_sentiment,
    'Gender volume': soc_gender_volume,
    'Sentiment number of results': soc_sentiment_number,
    'Sentiment authors': soc_sentiment_authors,
    'Sentiment locations': soc_sentiment_locations,
    'Sentiment languages': soc_sentiment_languages,
    'Sentiment by gender': soc_sentiment_gender,
    'Top keywords': soc_top_keywords,
    'Sentiment top keywords': soc_sentiment_keywords,
    'Sentiment diagram': soc_sentiment_number,
    'Authors by language': soc_author_language,
    'Authors by location': soc_author_location,
    'Authors by sentiment': soc_author_sentiment,
    'Authors by gender': soc_author_gender,
    'Top keywords by location': soc_keywords_location,
    'Top languages by location': soc_languages_location,
    'Top gender by location': soc_gender_location,
}
