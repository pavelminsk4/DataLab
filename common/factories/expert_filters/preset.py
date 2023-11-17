from common.factories.user import UserFactory
from expert_filters.models import Preset
from datetime import datetime
import factory


class PresetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Preset

    title      = factory.Faker('name')
    query      = ['cat OR dog', 'red OR blue']
    creator    = factory.SubFactory(UserFactory)
    updated_at = factory.LazyFunction(datetime.now)
    created_at = factory.LazyFunction(datetime.now)
