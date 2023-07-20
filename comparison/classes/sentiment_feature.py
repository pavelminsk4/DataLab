from project_social.widgets.sentiment.sentiment_top_keywords import calculate_for_sentiment_top_keywords as soc_top_keywords_by_sentiment
from project_social.widgets.sentiment.sentiment_number_of_results import calculate_for_sentiment_number_of_results as soc_sentiment
from project_social.widgets.dashboard.sentiment_languages import calculate_for_sentiment_languages as soc_sentiment_top_languages
from project_social.widgets.dashboard.sentiment_locations import calculate_for_sentiment_locations as soc_sentiment_by_locations
from project_social.widgets.dashboard.sentiment_authors import calculate_for_sentiment_authors as soc_sentiment_top_authors
from project_social.widgets.dashboard.sentiment import calculate_for_sentiment as soc_sentiment_by_period

from project_social.widgets.filters_for_widgets import posts_agregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_agregator as get_onl_posts

from project_social.models import ProjectSocial
from project.models import Project


class SentimentOnline:
    def __init__(self, project):
        self.posts = get_onl_posts(project)
        self.project = project

    def get_widgets(self):
        return {}


class SentimentSocial:
    def __init__(self, project):
        self.posts = get_soc_posts(project)
        self.project = project

    def get_widgets(self):
        return {
            'project_name': self.project.title,
            'widgets': [
                {'name': 'sentiment_number_of_results', 'data': soc_sentiment(self.posts)},
                {'name': 'sentiment', 'data': soc_sentiment(self.posts)},
                {'name': 'top_keywords_by_sentiment', 'data': soc_top_keywords_by_sentiment(self.posts)},
                {'name': 'sentiment_by_locations', 'data': soc_sentiment_by_locations(self.posts, 'day', 5)},
                {'name': 'sentiment_by_period', 'data': soc_sentiment_by_period(self.posts, 'day')},
                {'name': 'sentiment_top_languages', 'data': soc_sentiment_top_languages(self.posts, 'day', 5)},
                {'name': 'sentiment_top_authors', 'data': soc_sentiment_top_authors(self.posts, 'day', 5)},
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
