from project_social.widgets.sentiment.sentiment_number_of_results import calculate_for_sentiment_number_of_results as soc_sentiment
from project_social.widgets.dashboard.top_languages import calculate_for_top_languages as soc_top_languages
from project_social.widgets.dashboard.top_locations import calculate_for_top_locations as soc_top_locations
from project_social.widgets.dashboard.content_volume import calculate_for_content_volume as soc_volume
from project_social.widgets.dashboard.top_authors import calculate_for_top_authors as soc_top_authors
from project_social.widgets.dashboard.summary_widget import calculate_summary_widget as soc_summary
from common.social_keywords import get_keywords as soc_top_keywords

from widgets.sentiment.sentiment_number_of_results import get_sentiment_number_of_results as onl_sentiment
from widgets.common_widget.top_authors import post_agregator_top_auth_by_vol_widget as onl_top_authors
from widgets.common_widget.top_languages import post_aggregator_top_languages as onl_top_languages
from widgets.common_widget.top_countries import post_agregator_top_countries as onl_top_countries
from widgets.common_widget.top_sources import post_agregator_top_sources as onl_top_sources
from widgets.common_widget.volume_widget import post_agregator_volume as onl_volume
from widgets.summary.top_keywords import post_agg_top_keywords as onl_top_keywords
from widgets.common_widget.summary import calculate_summary_widget as onl_summary

from project_social.widgets.filters_for_widgets import posts_aggregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_with_filters as get_onl_posts

from project_social.models import ProjectSocial, SocialWidgetsList
from widgets.models import WidgetsList2
from project.models import Project


class SummaryFactory:
    def __init__(self, item):
        self.item = item

    def define(self):
        if self.item.module_type == 'Project':
            return SummaryOnline(Project.objects.get(id=self.item.module_project_id))
        else:
            return SummarySocial(ProjectSocial.objects.get(id=self.item.module_project_id))


class SummaryOnline:
    def __init__(self, project):
        self.posts = get_onl_posts(project, project.posts)
        self.project = project

    def get_widgets(self):
        widget_list = WidgetsList2.objects.get(project_id=self.project.pk)
        return {
            'project_name': self.project.title,
            'project_id': self.project.pk,
            'module': 'online',
            'widgets': [
                {'name': 'summary', 'widget_id': widget_list.summary_id, 'data': onl_summary(self.posts)},
                {'name': 'content_volume', 'widget_id': widget_list.volume_id, 'data': onl_volume(self.posts, 'day')},
                {'name': 'top_authors', 'widget_id': widget_list.top_authors_id, 'data': [{'user_name': elem['entry_author'], 'user_count': elem['author_posts_count']} for elem in onl_top_authors(self.posts, 5)]},
                {'name': 'sentiment', 'widget_id': widget_list.sentiment_for_period_id, 'data': onl_sentiment(self.posts)},
                {'name': 'top_sources', 'widget_id': widget_list.top_sources_id, 'data': onl_top_sources(self.posts, 5)},
                {'name': 'top_keywords', 'widget_id': widget_list.top_keywords_id, 'data': onl_top_keywords(self.posts)},
                {'name': 'top_languages', 'widget_id': widget_list.top_languages_id, 'data': onl_top_languages(self.posts, 5)},
                {'name': 'top_countries', 'widget_id': widget_list.top_countries_id, 'data': onl_top_countries(self.posts, 5)},
            ]
        }


class SummarySocial:
    def __init__(self, project):
        self.posts = get_soc_posts(project)
        self.project = project

    def get_widgets(self):
        widget_list = SocialWidgetsList.objects.get(project_id=self.project.pk)
        return {
            'project_name': self.project.title,
            'project_id': self.project.pk,
            'module': 'social',
            'widgets': [
                {'name': 'summary', 'widget_id': widget_list.summary_id, 'data': soc_summary(self.posts)},
                {'name': 'content_volume', 'widget_id': widget_list.content_volume_id, 'data': soc_volume(self.posts, 'day')},
                {'name': 'top_authors', 'widget_id': widget_list.top_authors_id, 'data': soc_top_authors(self.posts, 'day', 5)},
                {'name': 'sentiment', 'widget_id': widget_list.sentiment_id, 'data': soc_sentiment(self.posts)},
                {'name': 'top_keywords', 'widget_id': widget_list.top_keywords_id, 'data': soc_top_keywords(self.posts)},
                {'name': 'top_languages', 'widget_id': widget_list.top_languages_id, 'data': soc_top_languages(self.posts, 'day', 5)},
                {'name': 'top_locations', 'widget_id': widget_list.top_locations_id, 'data': soc_top_locations(self.posts, 'day', 5)},
            ]
        }
