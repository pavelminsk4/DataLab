from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.project import ProjectFactory
from comparison.models import ComparisonItem
import factory

class ComparisonItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ComparisonItem

    module_type       = 'Project'
    module_project_id = factory.SubFactory(ProjectFactory).id
    project           = factory.SubFactory(ProjectComparisonFactory)
