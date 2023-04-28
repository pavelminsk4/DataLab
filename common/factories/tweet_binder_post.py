import factory
from tweet_binder.models import TweetBinderPost


class TweetBinderPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TweetBinderPost

    post_id =        factory.Sequence(int)
    count_retweets = '1'
    count_favorites ='1'
    count_replies =  '1'
    language =       'En'
    user_name =      'First_name'
    user_alias =     '@first'
    locationString = 'Nostramo'
    sentiment =      'neutral'
    text =           'First twitter post'
    date =           '2020-10-10T00:00:00+00:00'
    creation_date =  '2020-10-10T00:00:00+00:00'
    type =           ['origin']
