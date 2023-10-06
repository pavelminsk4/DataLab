import factory
from tweet_binder.models import TweetBinderPost


class TweetBinderPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TweetBinderPost

    count_totalretweets = '1'
    count_retweets      = '1'
    count_favorites     = '1'
    count_replies       = '1'
    count_textlength    = '1'
    count_images        = '1'
    count_links         = '1'
    count_hashtags      = '1'
    language            = 'En'
    user_name           = 'First_name'
    user_alias          = 'First_name'
    user_gender         = 'male'
    locationString      = 'Nostramo'
    sentiment           = 'neutral'
    text                = 'First twitter post'
    date                = '2020-10-10T00:00:00Z'
    creation_date       = '2020-10-10T00:00:00Z'
    post_id             = factory.Sequence(int)
    language            = 'En'
    user_name           = 'First_name'
    user_followers      = '100'
    locationString      = 'Nostramo'
    type                = ['origin']
    videos              = ['www.video.com']
    hashtags            = ['test']
    user_value          = '100'
