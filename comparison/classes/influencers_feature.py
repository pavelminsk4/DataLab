from project_social.widgets.demography.top_authors_by_gender import calculate_for_top_authors_by_gender as soc_top_authors_by_gender
from project_social.widgets.influencers.authors_by_sentiment import calculate_for_authors_by_sentiment as soc_authors_by_sentiment
from project_social.widgets.demography.authors_by_language import calculate_for_authors_by_language as soc_authors_by_language
from project_social.widgets.demography.authors_by_location import calculate_for_authors_by_location as soc_authors_by_location
from project_social.widgets.demography.authors_by_gender import calculate_for_authors_by_gender as soc_authors_by_gender
from project_social.widgets.influencers.overall_top_authors import get_top_authors as soc_overall_top_authors
from project_social.widgets.influencers.top_sharing_sources import get_mosts as soc_top_sharing_sources

from project_social.widgets.filters_for_widgets import posts_agregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_agregator as get_onl_posts

from project_social.models import ProjectSocial
from project.models import Project


class InfluencersOnline:
    def __init__(self, project):
        self.posts = get_onl_posts(project)
        self.project = project

    def get_widgets(self):
        return {}


class InfluencersSocial:
    def __init__(self, project):
        self.posts = get_soc_posts(project)
        self.project = project

    def get_widgets(self):
        return {
            'project_name': self.project.title,
            'module': 'social',
            'widgets': [
                {'name': 'top_sharing_sources', 'data': soc_top_sharing_sources(self.posts)},
                {'name': 'authors_by_sentiment', 'data': soc_authors_by_sentiment(self.posts, 5)},
                {'name': 'overall_top_authors', 'data': soc_overall_top_authors(self.posts)},
                {'name': 'top_authors_by_gender', 'data': soc_top_authors_by_gender(self.posts)},
                {'name': 'authors_by_location', 'data': soc_authors_by_location(self.posts, 5)},
                {'name': 'authors_by_gender', 'data': soc_authors_by_gender(self.posts, 5)},
                {'name': 'authors_by_language', 'data': soc_authors_by_language(self.posts, 5)},
            ]
        }


class InfluencersFactory:
    def __init__(self, item):
        self.module_type = item.module_type
        self.project_id = item.module_project_id

    modules = {
        'Project':       {'model': Project, 'class': InfluencersOnline},
        'ProjectSocial': {'model': ProjectSocial, 'class': InfluencersSocial}
    }
    
    def define(self):
        module = self.modules[self.module_type]
        return module['class'](module['model'].objects.get(id=self.project_id))
