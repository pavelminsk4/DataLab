import factory
from project.models import Speech


class SpeechFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Speech

    language = 'English (United States)'
