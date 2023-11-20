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
    'Top languages by country': languages_country
}

def csv_view(request, project_pk, widget_pk):
    title = WidgetDescription.objects.get(id=widget_pk).title
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{Project.objects.get(id=project_pk).title}_{WidgetDescription.objects.get(id=widget_pk).title}.csv"'
    writer = csv.writer(response)
    fields, rows = widgets[title].to_csv(request, project_pk, widget_pk)
    writer.writerow(fields)
    for elem in rows:
        writer.writerow(elem)
    return response
