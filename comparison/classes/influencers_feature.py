from widgets.influencers.authors_by_sentiment import calculate_authors_by_sentiment as onl_authors_by_sentiment
from widgets.influencers.authors_by_language import calculate_authors_by_language as onl_authors_by_language
from widgets.demography.sources_by_language import calculate_sources_by_language as onl_sources_by_language
from widgets.influencers.authors_by_country import calculate_authors_by_country as onl_authors_by_location
from widgets.influencers.overall_top_authors import get_top_authors as onl_overall_top_authors
from widgets.demography.overall_top_sources import get_top_sources as onl_overall_top_sources
from widgets.demography.top_sharing_sources import get_mosts as onl_top_sharing_sources

from project_social.widgets.demography.top_authors_by_gender import calculate_for_top_authors_by_gender as soc_top_authors_by_gender
from project_social.widgets.influencers.authors_by_sentiment import calculate_for_authors_by_sentiment as soc_authors_by_sentiment
from project_social.widgets.demography.authors_by_language import calculate_for_authors_by_language as soc_authors_by_language
from project_social.widgets.demography.authors_by_location import calculate_for_authors_by_location as soc_authors_by_location
from project_social.widgets.demography.authors_by_gender import calculate_for_authors_by_gender as soc_authors_by_gender
from project_social.widgets.influencers.overall_top_authors import get_top_authors as soc_overall_top_authors
from project_social.widgets.influencers.top_sharing_sources import get_mosts as soc_top_sharing_sources

from project_social.widgets.filters_for_widgets import posts_agregator as get_soc_posts
from widgets.common_widget.filters_for_widgets import posts_with_filters as get_onl_posts

from project_social.models import ProjectSocial, SocialWidgetsList
from widgets.models import WidgetsList2
from project.models import Project


class InfluencersOnline:
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
                {'name': 'top_sharing_sources', 'widget_id':widget_list.top_sharing_sources_id, 'data': onl_top_sharing_sources(self.posts)},
                {'name': 'authors_by_language', 'widget_id':widget_list.authors_by_language_id, 'data': onl_authors_by_language(self.posts, 5)},
                {'name': 'overall_top_sources', 'widget_id':widget_list.overall_top_sources_id, 'data': onl_overall_top_sources(self.posts)},
                {'name': 'overall_top_authors', 'widget_id':widget_list.overall_top_authors_id, 'data': onl_overall_top_authors(self.posts)},
                {'name': 'authors_by_location', 'widget_id':widget_list.authors_by_country_id, 'data': onl_authors_by_location(self.posts, 5)},
                {'name': 'authors_by_sentiment', 'widget_id':widget_list.authors_by_sentiment_id, 'data': onl_authors_by_sentiment(self.posts, 5)},
                {'name': 'sources_by_language', 'widget_id':widget_list.sources_by_language_id, 'data': onl_sources_by_language(self.posts, 5)},
            ]
        }


class InfluencersSocial:
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
                {'name': 'top_sharing_sources', 'widget_id':widget_list.top_sharing_sources_id, 'data': soc_top_sharing_sources(self.posts)},
                {'name': 'authors_by_sentiment', 'widget_id':widget_list.authors_by_sentiment_id, 'data': soc_authors_by_sentiment(self.posts, 5)},
                {'name': 'overall_top_authors', 'widget_id':widget_list.overall_top_authors_id, 'data': soc_overall_top_authors(self.posts)},
                {'name': 'top_authors_by_gender', 'widget_id':widget_list.top_authors_by_gender_id, 'data': soc_top_authors_by_gender(self.posts)},
                {'name': 'authors_by_location', 'widget_id':widget_list.authors_by_location_id, 'data': soc_authors_by_location(self.posts, 5)},
                {'name': 'authors_by_gender', 'widget_id':widget_list.authors_by_gender_id, 'data': soc_authors_by_gender(self.posts, 5)},
                {'name': 'authors_by_language', 'widget_id':widget_list.authors_by_language_id, 'data': soc_authors_by_language(self.posts, 5)},
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
