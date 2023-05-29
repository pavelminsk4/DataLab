import factory
from twenty_four_seven.models import WorkspaceTwentyFourSeven
from ..department import DepartmentFactory


class WorkspaceTwentyFourSevenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkspaceTwentyFourSeven

    title = 'Datalab'
    department = factory.SubFactory(DepartmentFactory)
