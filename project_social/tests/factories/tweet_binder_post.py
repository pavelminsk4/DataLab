import factory
from datetime import datetime
from tweet_binder.models import TweetBinderPost

class TweetBinderPostFactory(factory.django.DjangoModelFactory):
  class Meta: 
    model = TweetBinderPost

  post_id=factory.Faker('pyint', min_value=0, max_value=1000)
  count_retweets='1'
  count_favorites='1'
  count_replies='1'
  language='En'
  user_name='First_name'
  user_alias='@first'
  locationString='Nostramo'
  sentiment='neutral'
  text='First twitter post'
  date=datetime(2020, 10, 10)
  creation_date=datetime(2020, 10, 10)
