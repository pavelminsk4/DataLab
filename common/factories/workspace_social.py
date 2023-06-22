from common.factories.department import DepartmentFactory
from project_social.models import WorkspaceSocial
import factory

class WorkspaceSocialFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = WorkspaceSocial

    title      = factory.Faker('name')
    department = factory.SubFactory(DepartmentFactory)
