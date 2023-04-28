import factory
from accounts.models import department


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = department

    departmentname =              factory.Faker('name')
    max_users =                   2
    max_projects =                2
    current_number_of_projects =  0
    current_number_of_users =     0
