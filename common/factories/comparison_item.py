from common.factories.project_comparison import ProjectComparisonFactory
from common.factories.project import ProjectFactory
from comparison.models import ComparisonItem
import factory


class ComparisonItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ComparisonItem
        exclude = ['pr']

    module_type       = 'Project'
    project           = factory.SubFactory(ProjectComparisonFactory)
    pr                = factory.SubFactory(ProjectFactory)
    module_project_id = factory.LazyAttribute(lambda o: o.pr.id)
