from project_social.widgets.sentiment.sentiment_top_keywords import calculate_for_sentiment_top_keywords as soc_top_keywords_by_location
from project_social.widgets.demography.languages_by_location import calculate as soc_top_languages_by_location
from project_social.widgets.dashboard.sentiment_locations import calculate as soc_sentiment_by_locations
from project_social.widgets.demography.authors_by_location import calculate as soc_authors_by_location
from project_social.widgets.demography.gender_by_location import calculate as soc_gender_by_location
from project_social.widgets.demography.authors_by_gender import calculate as soc_authors_by_gender
from common.social_keywords import get_keywords as soc_top_keywords

from project_social.widgets.filters_for_widgets import posts_agregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_agregator as get_onl_posts

from project_social.models import ProjectSocial
from project.models import Project


class DemographyOnline:
    def __init__(self, project):
        self.posts = get_onl_posts(project)
        self.project = project

    def get_widgets(self):
        return {}


class DemographySocial:
    def __init__(self, project):
        self.posts = get_soc_posts(project)
        self.project = project

    def get_widgets(self):
        return {
            'project_name': self.project.title,
            'widgets': [
                {'name': 'top_keywords', 'data': soc_top_keywords(self.posts)},
                {'name': 'top_keywords_by_location', 'data': soc_top_keywords_by_location(self.posts)},
                {'name': 'authors_by_location', 'data': soc_authors_by_location(self.posts, 5)},
                {'name': 'top_languages_by_location', 'data': soc_top_languages_by_location(self.posts, 5)},
                {'name': 'sentiment_by_locations', 'data': soc_sentiment_by_locations(self.posts, 'day', 5)},
                {'name': 'authors_by_gender', 'data': soc_authors_by_gender(self.posts, 5)},
                {'name': 'top_gender_by_location', 'data': soc_gender_by_location(self.posts, 5)},
            ]
        }


class DemographyFactory:
    def __init__(self, item):
        self.module_type = item.module_type
        self.project_id = item.module_project_id

    modules = {
        'Project':       {'model': Project, 'class': DemographyOnline},
        'ProjectSocial': {'model': ProjectSocial, 'class': DemographySocial}
    }
    
    def define(self):
        module = self.modules[self.module_type]
        return module['class'](module['model'].objects.get(id=self.project_id))
