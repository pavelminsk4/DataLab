from project_social.models import ProjectSocial
from common.factories.user import UserFactory
import factory


class ProjectSocialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectSocial

    title               = factory.Faker('name')
    keywords            = ['post', 'привет']
    additional_keywords = []
    ignore_keywords     = []
    start_search_date   = '2019-10-10T00:00:00Z'
    end_search_date     = '2023-10-10T00:00:00Z'
    creator             = factory.SubFactory(UserFactory)
