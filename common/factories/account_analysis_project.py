from account_analysis.models import ProjectAccountAnalysis
from common.factories.user import UserFactory
import factory


class AccountAnalysisProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectAccountAnalysis

    title =                factory.Faker('name')
    profile_handle =       'First_name'
    start_search_date =    '2019-10-10T00:00:00Z'
    end_search_date =      '2023-10-10T00:00:00Z'
    creator =              factory.SubFactory(UserFactory)
    language_dimensions =  []
    country_dimensions =   []
    source_dimensions =    []
    author_dimensions =    []
    sentiment_dimensions = []
