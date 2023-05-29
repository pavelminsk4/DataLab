import factory
from ..post import PostFactory
from twenty_four_seven.models import Item
from common.factories.twenty_four_seven.tfs_project import ProjectTwentyFourSevenFactory


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    online_post = factory.SubFactory(PostFactory)
    status = 'PCK'
    header = 'Header Text'
    text = 'Description Text'
    in_work = False
    is_back = False
    project = factory.SubFactory(ProjectTwentyFourSevenFactory)
