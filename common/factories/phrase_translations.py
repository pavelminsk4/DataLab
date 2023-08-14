from multilanguage.models import PhraseTranslations
import factory


class PhraseTranslationsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PhraseTranslations

    en = 'English Text'
    ar = None
