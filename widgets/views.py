from .common_widget.summary_widget import summary_widget
from .common_widget.volume_widget import volume
from .common_widget.clipping_feed_content_widget import cl_fd_cont_widg
from .common_widget.top_10_authors_by_volume_widget import top_10_auth_by_vol_widget
from .common_widget.top_10_brands_widget import top_10_brands
from .common_widget.top_10_countries_widget import top_10_countries
from .common_widget.top_10_languages_widget import top_10_languages
from .common_widget.content_volume_top_5_source_widget import content_volume_top_5_source
from .common_widget.sentiment_top_10_sources_widget import sentiment_top_10_sources
from .common_widget.sentiment_top_10_countries_widget import sentiment_top_10_countries
from .common_widget.sentiment_top_10_authors_widget import sentiment_top_10_authors
from .common_widget.sentiment_top_10_languages_widget import sentiment_top_10_languages
from .common_widget.content_volume_top_5_authors_widget import content_volume_top_5_authors
from .common_widget.content_volume_top_5_countries_widget import content_volume_top_5_countries
from .common_widget.sentiment_for_period_widget import sentiment_for_period
from .summary.top_keywords import top_keywords
from .sentiment.sentiment_top_keywords import sentiment_top_keywords
from .sentiment.sentiment_number_of_results import number_of_results
from .influencers.authors_by_country import get_authors_by_country
from .influencers.authors_by_language import get_authors_by_language
from .influencers.authors_by_sentiment import get_authors_by_sentiment
from .influencers.overall_top_authors import get_overall_top_authors
from .demography.sources_by_country import get_sources_by_country
from .demography.sources_by_language import get_sources_by_language
from .demography.overall_top_sources import get_overall_top_sources
from .demography.top_sharing_sources import get_top_sharing_sources
from .common_widget.dimensions_for_widgets import dimensions_for_each
from .common_widget.interactive_widgets import interactive_widgets

def sum_widget(request, pk, widget_pk):
  return summary_widget(pk, widget_pk)
def vol_widget(request, pk, widget_pk):
  return volume(request, pk, widget_pk)
def clipping_feed_content_widget(request, pk, widget_pk):
  return cl_fd_cont_widg(request, pk, widget_pk)
def top_10_authors_by_volume(request, pk, widget_pk):
  return top_10_auth_by_vol_widget(pk, widget_pk)
def top_10_brands_widget(request, pk, widget_pk):
  return top_10_brands(pk, widget_pk)
def top_10_countries_widget(request, pk, widget_pk):
  return top_10_countries(pk, widget_pk)
def top_10_languages_widget(request, pk, widget_pk):
  return top_10_languages(pk, widget_pk)
def content_volume_top_5_source_widget(request, pk, widget_pk):
  return content_volume_top_5_source(request, pk, widget_pk)
def sentiment_top_10_sources_widget(request, pk, widget_pk):
  return sentiment_top_10_sources(pk, widget_pk)
def sentiment_top_10_countries_widget(request, pk, widget_pk):
  return sentiment_top_10_countries(pk, widget_pk)
def sentiment_top_10_authors_widget(request, pk, widget_pk):
  return sentiment_top_10_authors(pk, widget_pk)
def sentiment_top_10_languages_widget(request, pk, widget_pk):
  return sentiment_top_10_languages(pk, widget_pk)
def sentiment_for_period_widget(request, pk, widget_pk):
  return sentiment_for_period(request, pk, widget_pk)
def content_volume_top_5_authors_widget(request, pk, widget_pk):
  return content_volume_top_5_authors(request, pk, widget_pk)
def content_volume_top_5_countries_widget(request, pk, widget_pk):
  return content_volume_top_5_countries(request, pk, widget_pk)
def top_keywords_widget(request, pk, widget_pk):
  return top_keywords(pk, widget_pk)
def sentiment_top_keywords_widget(request, pk, widget_pk):
  return sentiment_top_keywords(pk, widget_pk)
def sentiment_number_of_results(request, pk, widget_pk):
  return number_of_results(pk, widget_pk)
def sentiment_diagram(request, pk, widget_pk):
  return number_of_results(pk, widget_pk)
def authors_by_country(request, pk, widget_pk):
  return get_authors_by_country(pk, widget_pk)
def sources_by_country(request, pk, widget_pk):
  return get_sources_by_country(pk, widget_pk)
def sources_by_language(request, pk, widget_pk):
  return get_sources_by_language(pk, widget_pk)
def top_sharing_sources(request, pk, widget_pk):
  return get_top_sharing_sources(pk, widget_pk)
def overall_top_sources(request, pk, widget_pk):
  return get_overall_top_sources(pk, widget_pk)
def overall_top_authors(request, pk, widget_pk):
  return get_overall_top_authors(pk, widget_pk)
def authors_by_sentiment(request, pk, widget_pk):
  return get_authors_by_sentiment(pk, widget_pk)
def authors_by_language(request, pk, widget_pk):
  return get_authors_by_language(pk, widget_pk)
def dimensions_for_each_widgets(request, project_pk, widget_pk):
  return dimensions_for_each(request, widget_pk)
def interactive_data_for_widgets(request, project_pk, widget_pk):
  return interactive_widgets(request, project_pk, widget_pk)
