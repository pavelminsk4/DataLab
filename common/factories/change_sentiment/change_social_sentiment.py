from project_social.models import ChangingTweetbinderSentiment
import factory


class ChangingTweetbinderSentimentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChangingTweetbinderSentiment

    sentiment = 'positive' 
