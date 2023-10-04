from common.factories.twenty_four_seven.tfs_workspace import WorkspaceTwentyFourSevenFactory
from common.factories.twenty_four_seven.tfs_wa_recipient import WARecipient
from twenty_four_seven.models import ProjectTwentyFourSeven
from common.factories.user import UserFactory
import factory


class ProjectTwentyFourSevenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProjectTwentyFourSeven

    title = factory.Faker('name')
    keywords = ['Elon']
    additional_keywords = []
    ignore_keywords = []
    start_search_date = '2019-10-10T00:00:00Z'
    end_search_date = '2023-10-10T00:00:00Z'
    workspace = factory.SubFactory(WorkspaceTwentyFourSevenFactory)
    creator = factory.SubFactory(UserFactory)
    wa_recipient = factory.SubFactory(WARecipient)
