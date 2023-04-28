import factory
from project.models import Workspace
from .department import DepartmentFactory

class WorkspaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Workspace

    title =      'Sensika'
    department = factory.SubFactory(DepartmentFactory)
