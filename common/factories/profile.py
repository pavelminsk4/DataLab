from common.factories.department import DepartmentFactory
from common.factories.user import UserFactory
from accounts.models import Profile
import factory


class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile

    department = factory.SubFactory(DepartmentFactory)
    user       = factory.SubFactory(UserFactory)
