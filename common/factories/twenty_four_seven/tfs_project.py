import factory
from ..user import UserFactory
from twenty_four_seven.models import ProjectTwentyFourSeven
from common.factories.twenty_four_seven.tfs_workspace import WorkspaceTwentyFourSevenFactory


class ProjectTwentyFourSevenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectTwentyFourSeven

    title = factory.Faker('name')
    keywords = ['Elon']
    additional_keywords = []
    ignore_keywords = []
    start_search_date = '2019-10-10T00:00:00+00:00'
    end_search_date = '2023-10-10T00:00:00+00:00'
    workspace = factory.SubFactory(WorkspaceTwentyFourSevenFactory)
    creator = factory.SubFactory(UserFactory)
