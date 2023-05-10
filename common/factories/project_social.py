import factory
from .user import UserFactory
from project_social.models import ProjectSocial


class ProjectSocialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSocial

    title =                 factory.Faker('name')
    keywords =              ['post']
    additional_keywords =   []
    ignore_keywords =       []
    start_search_date =     '2019-10-10T00:00:00+00:00'
    end_search_date =       '2023-10-10T00:00:00+00:00'
    creator =               factory.SubFactory(UserFactory)
