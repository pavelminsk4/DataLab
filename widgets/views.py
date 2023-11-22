from .common_widget.content_volume_top_countries import content_volume_top_countries
from .common_widget.content_volume_top_authors import content_volume_top_authors
from .common_widget.content_volume_top_sources import content_volume_top_sources
from .demography.top_keywords_by_country import get_top_keywords_by_country
from .common_widget.sentiment_top_languages import sentiment_top_languages
from .common_widget.sentiment_top_countries import sentiment_top_countries
from .common_widget.sentiment_top_sources import sentiment_top_sources
from .common_widget.sentiment_top_authors import sentiment_top_authors
from .influencers.authors_by_sentiment import get_authors_by_sentiment
from .demography.languages_by_country import get_languages_by_country
from .common_widget.dimensions_for_widgets import dimensions_for_each
from .common_widget.sentiment_for_period import sentiment_for_period
from .sentiment.sentiment_top_keywords import sentiment_top_keywords
from .sentiment.sentiment_number_of_results import number_of_results
from .influencers.authors_by_language import get_authors_by_language
from .influencers.overall_top_authors import get_overall_top_authors
from .demography.sources_by_language import get_sources_by_language
from .demography.overall_top_sources import get_overall_top_sources
from .demography.top_sharing_sources import get_top_sharing_sources
from .common_widget.interactive_widgets import interactive_widgets
from .influencers.authors_by_country import get_authors_by_country
from .demography.sources_by_country import get_sources_by_country
from .common_widget.clipping_feed_content import cl_fd_cont_widg
from .common_widget.top_languages import top_languages
from .common_widget.top_countries import top_countries
from .common_widget.top_authors import top_authors
from .common_widget.summary import summary_widget
from .common_widget.top_sources import top_sources
from .common_widget.volume_widget import volume
from .summary.top_keywords import top_keywords


def onl_summary(request, pk, widget_pk):
    return summary_widget(request, pk, widget_pk)

def onl_volume(request, pk, widget_pk):
    return volume(request, pk, widget_pk)

def onl_clipping_feed_content(request, pk, widget_pk):
    return cl_fd_cont_widg(request, pk, widget_pk)

def onl_top_authors(request, pk, widget_pk):
    return top_authors(request,pk, widget_pk)

def onl_top_sources(request, pk, widget_pk):
    return top_sources(request, pk, widget_pk)

def onl_top_countries(request, pk, widget_pk):
    return top_countries(request, pk, widget_pk)

def onl_top_languages(request, pk, widget_pk):
    return top_languages(request, pk, widget_pk)

def onl_content_volume_top_sources(request, pk, widget_pk):
    return content_volume_top_sources(request, pk, widget_pk)

def onl_sentiment_top_sources(request, pk, widget_pk):
    return sentiment_top_sources(request, pk, widget_pk)

def onl_sentiment_top_countries(request, pk, widget_pk):
    return sentiment_top_countries(request, pk, widget_pk)

def onl_sentiment_top_authors(request, pk, widget_pk):
    return sentiment_top_authors(request, pk, widget_pk)

def onl_sentiment_top_languages(request, pk, widget_pk):
    return sentiment_top_languages(request, pk, widget_pk)

def onl_sentiment_for_period(request, pk, widget_pk):
    return sentiment_for_period(request, pk, widget_pk)

def onl_content_volume_top_authors(request, pk, widget_pk):
    return content_volume_top_authors(request, pk, widget_pk)

def onl_content_volume_top_countries(request, pk, widget_pk):
    return content_volume_top_countries(request, pk, widget_pk)

def onl_top_keywords(request, pk, widget_pk):
    return top_keywords(request, pk, widget_pk)

def onl_sentiment_top_keywords(request, pk, widget_pk):
    return sentiment_top_keywords(request, pk, widget_pk)

def onl_sentiment_number_of_results(request, pk, widget_pk):
    return number_of_results(request, pk, widget_pk)

def onl_sentiment_diagram(request, pk, widget_pk):
    return number_of_results(request, pk, widget_pk)

def onl_authors_by_country(request, pk, widget_pk):
    return get_authors_by_country(request, pk, widget_pk)

def onl_sources_by_country(request, pk, widget_pk):
    return get_sources_by_country(request, pk, widget_pk)

def onl_sources_by_language(request, pk, widget_pk):
    return get_sources_by_language(request, pk, widget_pk)

def onl_top_sharing_sources(request, pk, widget_pk):
    return get_top_sharing_sources(request, pk, widget_pk)

def onl_overall_top_sources(request, pk, widget_pk):
    return get_overall_top_sources(request, pk, widget_pk)

def onl_overall_top_authors(request, pk, widget_pk):
    return get_overall_top_authors(request, pk, widget_pk)

def onl_authors_by_sentiment(request, pk, widget_pk):
    return get_authors_by_sentiment(request, pk, widget_pk)

def onl_authors_by_language(request, pk, widget_pk):
    return get_authors_by_language(request, pk, widget_pk)

def onl_top_keywords_by_country(request, pk, widget_pk):
    return get_top_keywords_by_country(request, pk, widget_pk)

def onl_languages_by_country(request, pk, widget_pk):
    return get_languages_by_country(request, pk, widget_pk)

def dimensions_for_each_widgets(request, project_pk, widget_pk):
    return dimensions_for_each(request, widget_pk)

def interactive_data_for_widgets(request, project_pk, widget_pk):
    return interactive_widgets(request, project_pk, widget_pk)
