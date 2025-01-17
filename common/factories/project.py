import factory
from common.factories.user import UserFactory
from project.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title               = factory.Faker('name')
    keywords            = ['post', 'keyword']
    sources             = ['rss']
    additional_keywords = []
    ignore_keywords     = []
    status              = 'collecting_data'
    start_date          = '2019-10-10T00:00:00Z'
    start_search_date   = '2019-10-10T00:00:00Z'
    end_search_date     = '2023-10-10T00:00:00Z'
    creator             = factory.SubFactory(UserFactory)
    resume_offset       = 'earliest'
    synched_at          = None
