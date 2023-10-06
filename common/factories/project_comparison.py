from comparison.models import ProjectComparison
from common.factories.user import UserFactory
import factory


class ProjectComparisonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectComparison

    title      = factory.Faker('name')
    creator    = factory.SubFactory(UserFactory)
    created_at = '2019-10-10T00:00:00Z'
    updated_at = '2023-10-10T00:00:00Z'
