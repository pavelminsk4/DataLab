import factory
from project.models import Feedlinks


class FeedlinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Feedlinks

    source1 = factory.Faker('name')
    country = factory.Faker('country')
    sourceurl = factory.Faker('url')
