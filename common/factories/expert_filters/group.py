from common.factories.expert_filters.preset import PresetFactory 
from common.factories.user import UserFactory
from expert_filters.models import Group
from datetime import datetime
import factory


class GroupFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Group

    title       = factory.Faker('name')
    description = 'Description'
    creator     = factory.SubFactory(UserFactory)
    updated_at  = factory.LazyFunction(datetime.now)
    created_at  = factory.LazyFunction(datetime.now)
