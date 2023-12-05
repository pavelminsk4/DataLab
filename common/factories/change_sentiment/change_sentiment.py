from project.models import ChangingOnlineSentiment
import factory


class ChangingOnlineSentimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChangingOnlineSentiment

    sentiment = 'positive' 
