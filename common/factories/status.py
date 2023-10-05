import factory
from project.models import Status


class StatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Status

    progress = 1
