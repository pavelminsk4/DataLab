from project_social.widgets.sentiment.sentiment_top_keywords import calculate_for_sentiment_top_keywords as soc_top_keywords_by_sentiment
from project_social.widgets.sentiment.sentiment_number_of_results import calculate_for_sentiment_number_of_results as soc_sentiment
from project_social.widgets.dashboard.sentiment_languages import calculate_for_sentiment_languages as soc_sentiment_top_languages
from project_social.widgets.dashboard.sentiment_locations import calculate_for_sentiment_locations as soc_sentiment_by_locations
from project_social.widgets.dashboard.sentiment_authors import calculate_for_sentiment_authors as soc_sentiment_top_authors
from project_social.widgets.dashboard.sentiment import calculate_for_sentiment as soc_sentiment_by_period

from widgets.common_widget.sentiment_top_countries import post_aggregator_sentiment_top_countries as onl_sentiment_by_countries
from widgets.common_widget.sentiment_top_languages import post_agregator_sentiment_top_languages as onl_sentiment_top_languages
from widgets.common_widget.sentiment_top_authors import post_agregator_sentiment_top_authors as onl_sentiment_top_authors
from widgets.common_widget.sentiment_for_period import post_aggregator_sentiment_for_period as onl_sentiment_by_period
from widgets.sentiment.sentiment_top_keywords import post_agg_sentiment_top_keywords as onl_top_keywords_by_sentiment
from widgets.sentiment.sentiment_number_of_results import get_sentiment_number_of_results as onl_sentiment

from project_social.widgets.filters_for_widgets import posts_agregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_agregator as get_onl_posts

from project_social.models import ProjectSocial, SocialWidgetsList
from widgets.models import WidgetsList2
from project.models import Project


class SentimentOnline:
    def __init__(self, project):
        self.posts = get_onl_posts(project)
        self.project = project

    def get_widgets(self):
        widget_list = WidgetsList2.objects.get(project_id=self.project.pk)
        return {
            'project_name': self.project.title,
            'project_id': self.project.pk,
            'module': 'online',
            'widgets': [
                {'name': 'sentiment_number_of_results', 'widget_id':widget_list.sentiment_number_of_results_id, 'data': onl_sentiment(self.posts)},
                {'name': 'sentiment', 'widget_id':widget_list.sentiment_diagram_id, 'data': onl_sentiment(self.posts)},
                {'name': 'top_keywords_by_sentiment', 'widget_id':widget_list.sentiment_top_keywords_id, 'data': onl_top_keywords_by_sentiment(self.posts)},
                {'name': 'sentiment_by_locations', 'widget_id':widget_list.sentiment_top_countries_id, 'data': onl_sentiment_by_countries(self.posts, 5)},
                {'name': 'sentiment_by_period', 'widget_id':widget_list.sentiment_for_period_id, 'data': onl_sentiment_by_period(self.posts, 'day')},
                {'name': 'sentiment_top_languages', 'widget_id':widget_list.sentiment_top_languages_id, 'data': onl_sentiment_top_languages(self.posts, 5)},
                {'name': 'sentiment_top_authors', 'widget_id':widget_list.sentiment_top_authors_id, 'data': onl_sentiment_top_authors(self.posts, 5)},
            ]
        }


class SentimentSocial:
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
                {'name': 'sentiment_number_of_results', 'widget_id':widget_list.sentiment_number_of_results_id, 'data': soc_sentiment(self.posts)},
                {'name': 'sentiment', 'widget_id':widget_list.sentiment_id, 'data': soc_sentiment(self.posts)},
                {'name': 'top_keywords_by_sentiment', 'widget_id':widget_list.sentiment_top_keywords_id, 'data': soc_top_keywords_by_sentiment(self.posts)},
                {'name': 'sentiment_by_locations', 'widget_id':widget_list.sentiment_locations_id, 'data': soc_sentiment_by_locations(self.posts, 'day', 5)},
                {'name': 'sentiment_by_period', 'widget_id':widget_list.sentiment_id, 'data': soc_sentiment_by_period(self.posts, 'day')},
                {'name': 'sentiment_top_languages', 'widget_id':widget_list.sentiment_languages_id, 'data': soc_sentiment_top_languages(self.posts, 'day', 5)},
                {'name': 'sentiment_top_authors', 'widget_id':widget_list.sentiment_authors_id, 'data': soc_sentiment_top_authors(self.posts, 'day', 5)},
            ]
        }


class SentimentFactory:
    def __init__(self, item):
        self.module_type = item.module_type
        self.project_id = item.module_project_id

    modules = {
        'Project':       {'model': Project, 'class': SentimentOnline},
        'ProjectSocial': {'model': ProjectSocial, 'class': SentimentSocial}
    }
    
    def define(self):
        module = self.modules[self.module_type]
        return module['class'](module['model'].objects.get(id=self.project_id))
