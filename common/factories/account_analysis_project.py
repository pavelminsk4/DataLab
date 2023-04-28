import factory
from .user import UserFactory
from account_analysis.models import ProjectAccountAnalysis


class AccountAnalysisProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectAccountAnalysis

    title =                factory.Faker('name')
    profile_handle =       'First_name'
    start_search_date =    '2019-10-10T00:00:00+00:00'
    end_search_date =      '2023-10-10T00:00:00+00:00'
    creator =              factory.SubFactory(UserFactory)
    language_dimensions =  []
    country_dimensions =   []
    source_dimensions =    []
    author_dimensions =    []
    sentiment_dimensions = []
