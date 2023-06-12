from common.factories.department import DepartmentFactory
from comparison.models import WorkspaceComparison
import factory

class WorkspaceComparisonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkspaceComparison

    title      = factory.Faker('name')
    created_at = '2019-10-10T00:00:00+00:00'
    updated_at = '2023-10-10T00:00:00+00:00'
    department = factory.SubFactory(DepartmentFactory)
