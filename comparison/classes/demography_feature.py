from widgets.common_widget.sentiment_top_countries import post_aggregator_sentiment_top_countries as onl_sentiment_by_countries
from widgets.demography.languages_by_country import calculate_languages_by_country as onl_top_languages_by_country
from widgets.influencers.authors_by_country import calculate_authors_by_country as onl_top_authors_by_country
from widgets.demography.sources_by_country import calculate_sources_by_country as onl_top_sources_by_country
from widgets.summary.top_keywords import post_agg_top_keywords as onl_top_keywords

from project_social.widgets.demography.languages_by_location import calculate_for_languages_by_location as soc_top_languages_by_location
from project_social.widgets.dashboard.sentiment_locations import calculate_for_sentiment_locations as soc_sentiment_by_locations
from project_social.widgets.demography.authors_by_location import calculate_for_authors_by_location as soc_authors_by_location
from project_social.widgets.demography.gender_by_location import calculate_for_gender_by_location as soc_gender_by_location
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
        return {
            'project_name': self.project.title,
            'module': 'online',
            'widgets': [
                {'name': 'top_sources_by_country', 'data': onl_top_sources_by_country(self.posts, 5)},
                {'name': 'authors_by_location', 'data': onl_top_authors_by_country(self.posts, 5)},
                {'name': 'top_languages_by_location', 'data': onl_top_languages_by_country(self.posts, 5)},
                {'name': 'sentiment_by_locations', 'data': onl_sentiment_by_countries(self.posts, 5)},
                {'name': 'top_keywords', 'data':  onl_top_keywords(self.posts)},
            ]
        }


class DemographySocial:
    def __init__(self, project):
        self.posts = get_soc_posts(project)
        self.project = project

    def get_widgets(self):
        return {
            'project_name': self.project.title,
            'module': 'social',
            'widgets': [
                {'name': 'top_keywords', 'data': soc_top_keywords(self.posts)},
                {'name': 'authors_by_location', 'data': soc_authors_by_location(self.posts, 5)},
                {'name': 'top_languages_by_location', 'data': soc_top_languages_by_location(self.posts, 5)},
                {'name': 'sentiment_by_locations', 'data': soc_sentiment_by_locations(self.posts, 'day', 5)},
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
