from .talkwalker_feedlink import TalkwalkerFeedlinksFactory
from talkwalker.models import TalkwalkerPost
from .speech import SpeechFactory
import factory


class TalkwalkerPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TalkwalkerPost

    entry_title     = f"{factory.Faker('name')} post"
    feed_language   = factory.SubFactory(SpeechFactory)
    feedlink        = factory.SubFactory(TalkwalkerFeedlinksFactory)
    entry_published = '2020-10-10T00:00:00Z'
    entry_author    = 'Socrat'
    sentiment       = 'neutral'
    entry_summary   = 'post text'
