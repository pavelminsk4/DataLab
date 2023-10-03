import factory
from talkwalker.models import TalkwalkerFeedlink


class TalkwalkerFeedlinksFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TalkwalkerFeedlink

    source1 = factory.Faker('name')
    country = factory.Faker('country')
